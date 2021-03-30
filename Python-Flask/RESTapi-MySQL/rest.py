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
        tmp = {}
        tmp["id"]  = request.args.get('id')
        tmp["airline"]  = request.args.get('airline')
        tmp["airlineId"]  = request.args.get('airlineId')
        tmp["sourceAirport"]  = request.args.get('sourceAirport')
        tmp["sourceAirportId"]  = request.args.get('sourceAirportId')
        tmp["destinationAirport"]  = request.args.get('destinationAirport')
        tmp["destinationAirportId"]  = request.args.get('destinationAirportId')
        tmp["stops"]  = request.args.get('stops')
        tmp["equipment"]  = request.args.get('equipment')

        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM flightdata WHERE id LIKE '{tmp.get('id')}' OR airline LIKE '{tmp.get('airline')}' OR airlineId LIKE '{tmp.get('airlineId')}' OR sourceAirport LIKE '{tmp.get('sourceAirport')}' OR sourceAirportId LIKE '{tmp.get('sourceAirportId')}' OR destinationAirport LIKE '{tmp.get('destinationAirport')}' OR destinationAirportId LIKE '{tmp.get('destinationAirportId')}' OR stops LIKE '{tmp.get('stops')}' OR equipment LIKE '{tmp.get('equipment')}'")
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
        
        if flightdata:
            return jsonify(flightdata),200
        else:
            return jsonify({"message": "No flightdata matched the get request"}),404
    
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

        return jsonify(flightdata),200

@app.route('/', methods=['POST'])
def hello_worlda():
    return 'pöst!'