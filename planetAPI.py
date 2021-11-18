from flask import Flask, jsonify, request
import csv
 
app = Flask(__name__)

with open('planet_data.csv', newline="") as f:
  reader = csv.reader(f)
  planets_data = list(reader)



@app.route("/")
def MyDataAPI():
    return jsonify({
        "Data" : planets_data
    })

if __name__ == "__main__":
    app.run()