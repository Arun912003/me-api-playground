from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),   # ✅ THIS WAS MISSING
    path("api/", include("profileapi.urls")),
]
