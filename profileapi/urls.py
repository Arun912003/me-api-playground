from django.urls import path
from .views import health, profile_api, projects_by_skill

urlpatterns = [
    path("health/", health),
    path("profile/", profile_api),
    path("projects/", projects_by_skill),
]
