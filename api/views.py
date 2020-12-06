from rest_framework import generics
from api.serializers import RoomSerializer
from api.models import Room


class RoomView(generics.CreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

