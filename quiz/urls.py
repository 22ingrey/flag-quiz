"""
urls.py
-------
URL patterns for the quiz application.
Maps URL paths to their corresponding view functions.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('',          views.home,        name='home'),        # Main menu
    path('start/',    views.start_quiz,  name='start_quiz'),  # Initialise quiz
    path('quiz/',     views.quiz,        name='quiz'),         # Display question
    path('answer/',   views.answer,      name='answer'),       # Process answer
    path('results/',  views.results,     name='results'),      # Final score
]
