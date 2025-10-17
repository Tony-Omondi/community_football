from rest_framework import generics
from .models import Player
from .serializers import PlayerSerializer

# List all players or create a new one
class PlayerListCreateView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

# Retrieve, update, or delete a specific player
class PlayerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
