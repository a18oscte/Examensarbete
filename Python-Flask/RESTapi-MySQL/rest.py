from flask import Flask,request, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="examensarbete"
)

@app.route('/', methods=['GET'])
def get():
    if request.args:
        #id = request.args['id']
        return request.args
    else:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM flightdata")
        result = cursor.fetchall()
        flightdata = []
        for row in result:
            tmp = {}
            tmp["id"] = row[0]
            tmp["airline"] = row[1]
            tmp["airlineId"] = row[2]
            tmp["sourceAirport"] = row[3]
            tmp["sourceAirportId"] = row[4]
            tmp["destinationAirport"] = row[5]
            tmp["destinationAirportId"] = row[6]
            tmp["stops"] = row[7]
            tmp["equipment"] = row[8]
            flightdata.append(tmp)
        return jsonify(flightdata)

@app.route('/', methods=['POST'])
def hello_worlda():
    return 'pöst!'