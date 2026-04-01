# views.py
# Contains all the view functions for the Flag Quiz application.
# Each function handles a different page/URL in the quiz.

import random
from django.shortcuts import render, redirect
from .flag_data import FLAG_DATA


def generate_question(question_data, all_countries):
    # Builds a multiple choice question from a flag entry.
    # Parameters:
    #   question_data - a single flag dictionary with 'country' and 'flag'
    #   all_countries - list of all country names used to pick wrong answers
    # Returns a dictionary with the flag, correct answer, and 4 shuffled choices

    correct_answer = question_data['country']

    # Get a list of wrong answers by removing the correct one
    wrong_options = [c for c in all_countries if c != correct_answer]

    # Randomly pick 3 wrong answers
    wrong_answers = random.sample(wrong_options, 3)

    # Combine correct + wrong answers then shuffle
    choices = wrong_answers + [correct_answer]
    random.shuffle(choices)

    return {
        'flag': question_data['flag'],
        'correct_answer': correct_answer,
        'choices': choices,
    }


def home(request):
    # Displays the main menu page
    return render(request, 'quiz/home.html')


def start_quiz(request):
    # Starts a new quiz by shuffling questions and saving them to the session
    questions = list(FLAG_DATA)
    random.shuffle(questions)

    # Store quiz data in the session
    request.session['questions'] = questions
    request.session['current_index'] = 0
    request.session['score'] = 0
    request.session['total'] = len(questions)

    return redirect('quiz')


def quiz(request):
    # Displays the current question
    questions = request.session.get('questions', [])
    current_index = request.session.get('current_index', 0)
    score = request.session.get('score', 0)
    total = request.session.get('total', 0)

    # If no questions in session or quiz is finished, go to results
    if not questions or current_index >= total:
        return redirect('results')

    # Get the current flag data
    current_question = questions[current_index]

    # Get all country names for generating wrong answers
    all_countries = [q['country'] for q in FLAG_DATA]

    # Generate the multiple choice question using the subprogram
    question = generate_question(current_question, all_countries)

    # Store the correct answer in the session so it never appears in the HTML
    request.session['correct_answer'] = question['correct_answer']

    context = {
        'flag': question['flag'],
        'choices': question['choices'],
        'question_number': current_index + 1,
        'total': total,
        'score': score,
    }

    return render(request, 'quiz/quiz.html', context)


def answer(request):
    # Handles the submitted answer from the quiz form
    if request.method == 'POST':
        selected = request.POST.get('selected_answer', '')

        # Get the correct answer from the session, not from the form
        correct = request.session.get('correct_answer', '')

        # Check if the answer is correct and update the score
        if selected == correct:
            request.session['score'] = request.session.get('score', 0) + 1

        # Move to the next question
        request.session['current_index'] = request.session.get('current_index', 0) + 1

        # If all questions are done, go to results page
        if request.session['current_index'] >= request.session.get('total', 0):
            return redirect('results')

        return redirect('quiz')

    return redirect('quiz')


def results(request):
    # Displays the final score screen
    score = request.session.get('score', 0)
    total = request.session.get('total', 0)

    # Calculate percentage score
    if total > 0:
        percentage = round((score / total) * 100)
    else:
        percentage = 0

    # Choose a feedback message based on the score
    if percentage >= 80:
        message = 'Excellent work!'
    elif percentage >= 50:
        message = 'Good effort, keep practising!'
    else:
        message = 'Keep trying, you will improve!'

    context = {
        'score': score,
        'total': total,
        'percentage': percentage,
        'message': message,
    }

    return render(request, 'quiz/results.html', context)