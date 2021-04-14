from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from RESTapi.models import Flightdata
import json

@csrf_exempt
def homePageView(request):
    #If there is a get request
    if request.method == 'GET':
        #Get the parameters
        data = request.GET
        #If there is inparameters
        if data:
            return JsonResponse(data.dict())
        
        #If there is no inparameters
        else:
            #Gets the data from the database
            flightdata = [entry for entry in Flightdata.objects.values() ]
            return JsonResponse(flightdata, safe=False)

    #If there is a post request
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse(data)
