from rest_framework import generics
from .models import Team
from .serializers import TeamSerializer

# List all teams or create a new one
class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


# Retrieve, update, or delete a specific team
class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
