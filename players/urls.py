from django.urls import path
from .views import PlayerListCreateView, PlayerDetailView

urlpatterns = [
    path('', PlayerListCreateView.as_view(), name='player-list'),
    path('<int:pk>/', PlayerDetailView.as_view(), name='player-detail'),
]
