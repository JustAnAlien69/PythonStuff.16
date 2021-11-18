from flask import Flask, jsonify, request
import csv
 
app = Flask(__name__)

with open('planet_data.csv', newline="") as f:
  reader = csv.reader(f)
  planets_data = list(reader)

with open('terrestial.csv', newline="") as f:
  reader = csv.reader(f)
  terrestial_data = list(reader)

@app.route("/")
def MyDataAPI():
    return jsonify({
        "Data" : planets_data
    })

@app.route("/terrestial")
def TerrestialData():
    return jsonify({
        "Data" : terrestial_data
    })

if __name__ == "__main__":
    app.run()