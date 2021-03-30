from flask import Flask,request, jsonify
import mysql.connector
import json

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
def post():
    if request.data:
        data = json.loads(request.data)
        cursor = db.cursor()
        query = "INSERT INTO flightdata SET airline=%s, airlineId=%s, sourceAirport=%s, sourceAirportId=%s, destinationAirport=%s, destinationAirportId=%s, stops=%s, equipment=%s";
        val = (data["airline"], data["airlineId"], data["sourceAirport"], data["sourceAirportId"], data["destinationAirport"], data["destinationAirportId"], data["stops"], data["equipment"])
        cursor.execute(query, val)
        
        try:
            db.commit()
            return jsonify({"message": "flightdata was created."}),200

        except mysql.connector.Error as error :
            return jsonify({"message": "Unable to create flightdata."}),503

    else:
        return jsonify({"message": "Unable to create flightdata. Data is incomplete."}),204