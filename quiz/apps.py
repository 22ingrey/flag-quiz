"""
apps.py
-------
Application configuration for the quiz app.
"""

from django.apps import AppConfig


class QuizConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quiz'
