from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    # path('api/tournaments/', include('tournaments.urls')),
    # path('api/teams/', include('teams.urls')),
    # path('api/players/', include('players.urls')),
    # path('api/matches/', include('matches.urls')),
    # path('api/standings/', include('standings.urls')),
]
