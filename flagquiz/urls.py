"""
URL configuration for the flagquiz project.
All URL patterns are delegated to the quiz application.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),         # Django admin panel
    path('', include('quiz.urls')),          # Quiz app handles all other routes
]
