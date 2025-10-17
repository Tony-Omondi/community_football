from django.urls import path
from .views import StandingListCreateView, StandingDetailView

urlpatterns = [
    path('', StandingListCreateView.as_view(), name='standing-list-create'),
    path('<int:pk>/', StandingDetailView.as_view(), name='standing-detail'),
]
