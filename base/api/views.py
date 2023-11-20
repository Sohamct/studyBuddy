from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

# @api_view('GET', 'PUT', 'POST')
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    # return JsonResponse(routes, safe=False)
    return Response(routes)
# safe=False means we can use more than python dictionaries in jsonResponse

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)


""" CORS: cross origin resource sharing
if we try to request the django usrls from different resource it does not allows.
--> we can either allow all urls to access from outside resources or not at all or a set of urls to request it.


search for django cors header
"""
