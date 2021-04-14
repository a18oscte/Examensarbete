from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from RESTapi.models import Flightdata
from django.db.models import Q
import json

@csrf_exempt
def homePageView(request):
    #If there is a get request
    if request.method == 'GET':
        #Get the parameters
        data = request.GET
        #If there is inparameters
        if data:
            #Get the matching fligtdata from the database
            FlightdataQuerySet = Flightdata.objects.filter(Q(id=data.get("id", False)) | Q(airline=data.get("airline", False)) | Q(airlineid=data.get("airlineId", False)) | Q(sourceairport=data.get("sourceAirport", False)) | Q(sourceairportid=data.get("sourceAirportId", False)) | Q(destinationairport=data.get("destinationAirport", False)) | Q(destinationairportid=data.get("destinationAirportId", False)) | Q(stops=data.get("stops", None)) | Q(equipment=data.get("equipment", False)))
            #If there is no matching flightdata in the database
            if not FlightdataQuerySet:
                return JsonResponse({"message": "No flightdata matched the get request"}, safe=False, status=404)
            #If there is matching flightdata in the database
            else:
                #converts the Query set to a list with dictionarys
                flightdata = [entry for entry in FlightdataQuerySet.values() ]
                #responed with the list with the flightdata
                return JsonResponse(flightdata, safe=False, status=200)
    
        #If there is no inparameters
        else:
            #Gets the data from the database
            flightdata = [entry for entry in Flightdata.objects.values() ]
            #responed with the list with the flightdata
            return JsonResponse(flightdata, safe=False, status=200)

    #If there is a post request
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse(data)
