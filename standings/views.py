from rest_framework import generics
from .models import Standing
from .serializers import StandingSerializer

class StandingListCreateView(generics.ListCreateAPIView):
    queryset = Standing.objects.all()
    serializer_class = StandingSerializer

class StandingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Standing.objects.all()
    serializer_class = StandingSerializer
