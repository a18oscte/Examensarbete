from flask import Flask,request, jsonify
import mysql.connector
import json

app = Flask(__name__)

#Create database connection
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="examensarbete"
)

#If there is a get request
@app.route('/', methods=['GET'])
def get():
    #If there is inparameters
    if request.args:
        #Get the inparameters into an dictionary
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

        #Get the matching fligtdata from the database
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM flightdata WHERE id LIKE '{tmp.get('id')}' OR airline LIKE '{tmp.get('airline')}' OR airlineId LIKE '{tmp.get('airlineId')}' OR sourceAirport LIKE '{tmp.get('sourceAirport')}' OR sourceAirportId LIKE '{tmp.get('sourceAirportId')}' OR destinationAirport LIKE '{tmp.get('destinationAirport')}' OR destinationAirportId LIKE '{tmp.get('destinationAirportId')}' OR stops LIKE '{tmp.get('stops')}' OR equipment LIKE '{tmp.get('equipment')}'")
        result = cursor.fetchall()

        #adding flightdata to a list
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

        #If there is matching flightdata in the database
        if flightdata:
            #responed with the list with the flightdata
            return jsonify(flightdata),200
        #If there is no matching flightdata in the database
        else:
            return jsonify({"message": "No flightdata matched the get request"}),404
    
    #If there is no inparameters
    else:
        #Get all flightdatafrom the darabase
        cursor = db.cursor()
        cursor.execute("SELECT * FROM flightdata")
        result = cursor.fetchall()

        #Adding flightdata to a list
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

        #Responed with the list with all flightdata
        return jsonify(flightdata),200

#If there is a post request
@app.route('/', methods=['POST'])
def post():

    #Only works if there is in-data
    if request.data:

        #converts in-data to a dictionary 
        data = json.loads(request.data)

        #if there is multiple flightdata objects in the data
        if type(data) == list:
            #loops throut the flightdata
            for obj in data:
                #Preparing the sql statement with the in-data
                cursor = db.cursor()
                query = "INSERT INTO flightdata SET airline=%s, airlineId=%s, sourceAirport=%s, sourceAirportId=%s, destinationAirport=%s, destinationAirportId=%s, stops=%s, equipment=%s";
                val = (obj["airline"], obj["airlineId"], obj["sourceAirport"], obj["sourceAirportId"], obj["destinationAirport"], obj["destinationAirportId"], obj["stops"], obj["equipment"])
                cursor.execute(query, val)

                #Executes the sql statement and checks for errors
                try:
                    db.commit()

                except mysql.connector.Error as error :
                    return jsonify({"message": "Unable to create flightdata."}),503
                
            return jsonify({"message": "flightdata was created."}),200
        
        #if there is one flightdata object in the data
        else:
            #Preparing the sql statement with the in-data
            cursor = db.cursor()
            query = "INSERT INTO flightdata SET airline=%s, airlineId=%s, sourceAirport=%s, sourceAirportId=%s, destinationAirport=%s, destinationAirportId=%s, stops=%s, equipment=%s";
            val = (data["airline"], data["airlineId"], data["sourceAirport"], data["sourceAirportId"], data["destinationAirport"], data["destinationAirportId"], data["stops"], data["equipment"])
            cursor.execute(query, val)
        
            #Executes the sql statement and checks for errors
            try:
                db.commit()
                return jsonify({"message": "flightdata was created."}),200

            except mysql.connector.Error as error :
                return jsonify({"message": "Unable to create flightdata."}),503

    #Respones if there is no in-data
    else:
        return jsonify({"message": "Unable to create flightdata. Data is incomplete."}),204
