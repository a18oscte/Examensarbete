from flask import Flask,request, jsonify
import json

app = Flask(__name__)

tmp = '[ { "airline": "2B", "airlineId": "410", "sourceAirport": "AER", "sourceAirportId": "2965", "destinationAirport": "KZN", "destinationAirportId": "2990", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "ASF", "sourceAirportId": "2966", "destinationAirport": "KZN", "destinationAirportId": "2990", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "ASF", "sourceAirportId": "2966", "destinationAirport": "MRV", "destinationAirportId": "2962", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "CEK", "sourceAirportId": "2968", "destinationAirport": "KZN", "destinationAirportId": "2990", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "CEK", "sourceAirportId": "2968", "destinationAirport": "OVB", "destinationAirportId": "4078", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "DME", "sourceAirportId": "4029", "destinationAirport": "KZN", "destinationAirportId": "2990", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "DME", "sourceAirportId": "4029", "destinationAirport": "NBC", "destinationAirportId": "6969", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "DME", "sourceAirportId": "4029", "destinationAirport": "TGK", "destinationAirportId": null, "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "DME", "sourceAirportId": "4029", "destinationAirport": "UUA", "destinationAirportId": "6160", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "EGO", "sourceAirportId": "6156", "destinationAirport": "KGD", "destinationAirportId": "2952", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "EGO", "sourceAirportId": "6156", "destinationAirport": "KZN", "destinationAirportId": "2990", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "GYD", "sourceAirportId": "2922", "destinationAirport": "NBC", "destinationAirportId": "6969", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "KGD", "sourceAirportId": "2952", "destinationAirport": "EGO", "destinationAirportId": "6156", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "KZN", "sourceAirportId": "2990", "destinationAirport": "AER", "destinationAirportId": "2965", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "KZN", "sourceAirportId": "2990", "destinationAirport": "ASF", "destinationAirportId": "2966", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "KZN", "sourceAirportId": "2990", "destinationAirport": "CEK", "destinationAirportId": "2968", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "KZN", "sourceAirportId": "2990", "destinationAirport": "DME", "destinationAirportId": "4029", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "KZN", "sourceAirportId": "2990", "destinationAirport": "EGO", "destinationAirportId": "6156", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "KZN", "sourceAirportId": "2990", "destinationAirport": "LED", "destinationAirportId": "2948", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "KZN", "sourceAirportId": "2990", "destinationAirport": "SVX", "destinationAirportId": "2975", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "LED", "sourceAirportId": "2948", "destinationAirport": "KZN", "destinationAirportId": "2990", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "LED", "sourceAirportId": "2948", "destinationAirport": "NBC", "destinationAirportId": "6969", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "LED", "sourceAirportId": "2948", "destinationAirport": "UUA", "destinationAirportId": "6160", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "MRV", "sourceAirportId": "2962", "destinationAirport": "ASF", "destinationAirportId": "2966", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "NBC", "sourceAirportId": "6969", "destinationAirport": "DME", "destinationAirportId": "4029", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "NBC", "sourceAirportId": "6969", "destinationAirport": "GYD", "destinationAirportId": "2922", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "NBC", "sourceAirportId": "6969", "destinationAirport": "LED", "destinationAirportId": "2948", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "NBC", "sourceAirportId": "6969", "destinationAirport": "SVX", "destinationAirportId": "2975", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "NJC", "sourceAirportId": "2972", "destinationAirport": "SVX", "destinationAirportId": "2975", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "NJC", "sourceAirportId": "2972", "destinationAirport": "UUA", "destinationAirportId": "6160", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "NUX", "sourceAirportId": "4364", "destinationAirport": "SVX", "destinationAirportId": "2975", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "OVB", "sourceAirportId": "4078", "destinationAirport": "CEK", "destinationAirportId": "2968", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "OVB", "sourceAirportId": "4078", "destinationAirport": "SVX", "destinationAirportId": "2975", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "SVX", "sourceAirportId": "2975", "destinationAirport": "KZN", "destinationAirportId": "2990", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "SVX", "sourceAirportId": "2975", "destinationAirport": "NBC", "destinationAirportId": "6969", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "SVX", "sourceAirportId": "2975", "destinationAirport": "NJC", "destinationAirportId": "2972", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "SVX", "sourceAirportId": "2975", "destinationAirport": "NUX", "destinationAirportId": "4364", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "SVX", "sourceAirportId": "2975", "destinationAirport": "OVB", "destinationAirportId": "4078", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "TGK", "sourceAirportId": null, "destinationAirport": "DME", "destinationAirportId": "4029", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "UUA", "sourceAirportId": "6160", "destinationAirport": "DME", "destinationAirportId": "4029", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "UUA", "sourceAirportId": "6160", "destinationAirport": "LED", "destinationAirportId": "2948", "stops": 0, "equipment": "CR2" }, { "airline": "2B", "airlineId": "410", "sourceAirport": "UUA", "sourceAirportId": "6160", "destinationAirport": "NJC", "destinationAirportId": "2972", "stops": 0, "equipment": "CR2" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "BTK", "sourceAirportId": "2936", "destinationAirport": "IKT", "destinationAirportId": "2937", "stops": 0, "equipment": "A81" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "BTK", "sourceAirportId": "2936", "destinationAirport": "OVB", "destinationAirportId": "4078", "stops": 0, "equipment": "A81" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "CEK", "sourceAirportId": "2968", "destinationAirport": "OVB", "destinationAirportId": "4078", "stops": 0, "equipment": "A81" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "HTA", "sourceAirportId": "2935", "destinationAirport": "IKT", "destinationAirportId": "2937", "stops": 0, "equipment": "AN4" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "IKT", "sourceAirportId": "2937", "destinationAirport": "BTK", "destinationAirportId": "2936", "stops": 0, "equipment": "A81" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "IKT", "sourceAirportId": "2937", "destinationAirport": "HTA", "destinationAirportId": "2935", "stops": 0, "equipment": "AN4" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "IKT", "sourceAirportId": "2937", "destinationAirport": "KCK", "destinationAirportId": null, "stops": 0, "equipment": "AN4" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "IKT", "sourceAirportId": "2937", "destinationAirport": "ODO", "destinationAirportId": "8944", "stops": 0, "equipment": "AN4" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "IKT", "sourceAirportId": "2937", "destinationAirport": "OVB", "destinationAirportId": "4078", "stops": 0, "equipment": "A81" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "IKT", "sourceAirportId": "2937", "destinationAirport": "UKX", "destinationAirportId": "6924", "stops": 0, "equipment": "AN4" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "IKT", "sourceAirportId": "2937", "destinationAirport": "ULK", "destinationAirportId": "9026", "stops": 0, "equipment": "AN4" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "IKT", "sourceAirportId": "2937", "destinationAirport": "YKS", "destinationAirportId": "2923", "stops": 0, "equipment": "A81" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "KCK", "sourceAirportId": null, "destinationAirport": "IKT", "destinationAirportId": "2937", "stops": 0, "equipment": "AN4" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "MJZ", "sourceAirportId": "2925", "destinationAirport": "OVB", "destinationAirportId": "4078", "stops": 0, "equipment": "A81" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "ODO", "sourceAirportId": "8944", "destinationAirport": "IKT", "destinationAirportId": "2937", "stops": 0, "equipment": "AN4" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "OVB", "sourceAirportId": "4078", "destinationAirport": "BTK", "destinationAirportId": "2936", "stops": 0, "equipment": "A81" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "OVB", "sourceAirportId": "4078", "destinationAirport": "CEK", "destinationAirportId": "2968", "stops": 0, "equipment": "A81" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "OVB", "sourceAirportId": "4078", "destinationAirport": "IKT", "destinationAirportId": "2937", "stops": 0, "equipment": "A81" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "UKX", "sourceAirportId": "6924", "destinationAirport": "IKT", "destinationAirportId": "2937", "stops": 0, "equipment": "AN4" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "ULK", "sourceAirportId": "9026", "destinationAirport": "IKT", "destinationAirportId": "2937", "stops": 0, "equipment": "AN4" }, { "airline": "2G", "airlineId": "1654", "sourceAirport": "YKS", "sourceAirportId": "2923", "destinationAirport": "IKT", "destinationAirportId": "2937", "stops": 0, "equipment": "A81" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "AYP", "sourceAirportId": "2786", "destinationAirport": "LIM", "destinationAirportId": "2789", "stops": 0, "equipment": "142" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "CUZ", "sourceAirportId": "2812", "destinationAirport": "LIM", "destinationAirportId": "2789", "stops": 0, "equipment": "142 141" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "CUZ", "sourceAirportId": "2812", "destinationAirport": "PEM", "destinationAirportId": "2808", "stops": 0, "equipment": "142" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "HUU", "sourceAirportId": "6067", "destinationAirport": "LIM", "destinationAirportId": "2789", "stops": 0, "equipment": "141" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "IQT", "sourceAirportId": "2801", "destinationAirport": "PCL", "destinationAirportId": "2781", "stops": 0, "equipment": "143" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "IQT", "sourceAirportId": "2801", "destinationAirport": "TPP", "destinationAirportId": "2806", "stops": 0, "equipment": "142" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "LIM", "sourceAirportId": "2789", "destinationAirport": "AYP", "destinationAirportId": "2786", "stops": 0, "equipment": "142" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "LIM", "sourceAirportId": "2789", "destinationAirport": "CUZ", "destinationAirportId": "2812", "stops": 0, "equipment": "142 141" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "LIM", "sourceAirportId": "2789", "destinationAirport": "HUU", "destinationAirportId": "6067", "stops": 0, "equipment": "141" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "LIM", "sourceAirportId": "2789", "destinationAirport": "PCL", "destinationAirportId": "2781", "stops": 0, "equipment": "143 146" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "LIM", "sourceAirportId": "2789", "destinationAirport": "TPP", "destinationAirportId": "2806", "stops": 0, "equipment": "142 146" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "PCL", "sourceAirportId": "2781", "destinationAirport": "IQT", "destinationAirportId": "2801", "stops": 0, "equipment": "143" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "PCL", "sourceAirportId": "2781", "destinationAirport": "LIM", "destinationAirportId": "2789", "stops": 0, "equipment": "143 146" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "PCL", "sourceAirportId": "2781", "destinationAirport": "TPP", "destinationAirportId": "2806", "stops": 0, "equipment": "146" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "PEM", "sourceAirportId": "2808", "destinationAirport": "CUZ", "destinationAirportId": "2812", "stops": 0, "equipment": "142" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "TPP", "sourceAirportId": "2806", "destinationAirport": "IQT", "destinationAirportId": "2801", "stops": 0, "equipment": "142" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "TPP", "sourceAirportId": "2806", "destinationAirport": "LIM", "destinationAirportId": "2789", "stops": 0, "equipment": "142 146" }, { "airline": "2I", "airlineId": "8359", "sourceAirport": "TPP", "sourceAirportId": "2806", "destinationAirport": "PCL", "destinationAirportId": "2781", "stops": 0, "equipment": "146" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "ABJ", "sourceAirportId": "253", "destinationAirport": "BOY", "destinationAirportId": "247", "stops": 0, "equipment": "CRJ" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "ABJ", "sourceAirportId": "253", "destinationAirport": "OUA", "destinationAirportId": "246", "stops": 0, "equipment": "E70 CRJ M87" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "ACC", "sourceAirportId": "248", "destinationAirport": "OUA", "destinationAirportId": "246", "stops": 0, "equipment": "CRJ" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "BKO", "sourceAirportId": "1044", "destinationAirport": "ABJ", "destinationAirportId": "253", "stops": 0, "equipment": "M87" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "BKO", "sourceAirportId": "1044", "destinationAirport": "DKR", "destinationAirportId": "1084", "stops": 0, "equipment": "M87" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "BKO", "sourceAirportId": "1044", "destinationAirport": "OUA", "destinationAirportId": "246", "stops": 0, "equipment": "CRJ" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "BOY", "sourceAirportId": "247", "destinationAirport": "ABJ", "destinationAirportId": "253", "stops": 0, "equipment": "CRJ" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "BOY", "sourceAirportId": "247", "destinationAirport": "OUA", "destinationAirportId": "246", "stops": 0, "equipment": "CRJ" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "COO", "sourceAirportId": "245", "destinationAirport": "LFW", "destinationAirportId": "298", "stops": 0, "equipment": "M87" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "COO", "sourceAirportId": "245", "destinationAirport": "OUA", "destinationAirportId": "246", "stops": 0, "equipment": "M87" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "DKR", "sourceAirportId": "1084", "destinationAirport": "BKO", "destinationAirportId": "1044", "stops": 0, "equipment": "M87" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "DKR", "sourceAirportId": "1084", "destinationAirport": "OUA", "destinationAirportId": "246", "stops": 0, "equipment": "M87" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "LFW", "sourceAirportId": "298", "destinationAirport": "OUA", "destinationAirportId": "246", "stops": 0, "equipment": "M87 CRJ" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "NIM", "sourceAirportId": "280", "destinationAirport": "OUA", "destinationAirportId": "246", "stops": 0, "equipment": "CRJ" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "OUA", "sourceAirportId": "246", "destinationAirport": "ABJ", "destinationAirportId": "253", "stops": 0, "equipment": "E70 CRJ M87" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "OUA", "sourceAirportId": "246", "destinationAirport": "ACC", "destinationAirportId": "248", "stops": 0, "equipment": "CRJ" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "OUA", "sourceAirportId": "246", "destinationAirport": "BKO", "destinationAirportId": "1044", "stops": 0, "equipment": "M87 CRJ" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "OUA", "sourceAirportId": "246", "destinationAirport": "BOY", "destinationAirportId": "247", "stops": 0, "equipment": "CRJ" }, { "airline": "2J", "airlineId": "470", "sourceAirport": "OUA", "sourceAirportId": "246", "destinationAirport": "COO", "destinationAirportId": "245", "stops": 0, "equipment": "M87" } ]'
flightdata = json.loads(tmp)

@app.route('/', methods=['GET'])
def get():
    if request.args:
        tmpflightdata = {}
        i = 0
        
        for tmp in flightdata:
            if request.args.get('airline') and request.args.get('airline') == tmp['airline']:
                i += 1
                tmpflightdata[i] = tmp
                continue
            if request.args.get('airlineId') and request.args.get('airlineId') == tmp['airlineId']:
                i += 1
                tmpflightdata[i] = tmp
                continue
            if request.args.get('sourceAirport') and request.args.get('sourceAirport') == tmp['sourceAirport']:
                i += 1
                tmpflightdata[i] = tmp
                continue
            if request.args.get('sourceAirportId') and request.args.get('sourceAirportId') == tmp['sourceAirportId']:
                i += 1
                tmpflightdata[i] = tmp
                continue
            if request.args.get('destinationAirport') and request.args.get('destinationAirport') == tmp['destinationAirport']:
                i += 1
                tmpflightdata[i] = tmp
                continue
            if request.args.get('destinationAirportId') and request.args.get('destinationAirportId') == tmp['destinationAirportId']:
                i += 1
                tmpflightdata[i] = tmp
                continue
            if request.args.get('stops') and request.args.get('stops') == tmp['stops']:
                i += 1
                tmpflightdata[i] = tmp
                continue
            if request.args.get('equipment') and request.args.get('equipment') == tmp['equipment']:
                i += 1
                tmpflightdata[i] = tmp
                continue

        if tmpflightdata:
            return jsonify(tmpflightdata),200
        else:
            return jsonify({"message": "No flightdata matched the get request"}),404

    else:
        return jsonify(flightdata),200
