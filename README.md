# 🌍 Flag Geography Quiz
### A Django web application for secondary geography students

---

## Setup Instructions

### 1. Install Python 3.12+
Download from https://python.org and make sure to tick **"Add Python to PATH"** during install.

### 2. Install Django
Open a terminal (or VS Code terminal) and run:
```
pip install -r requirements.txt
```

### 3. Set up the database
Django needs to create session tables. Run:
```
python manage.py migrate
```

### 4. Run the development server
```
python manage.py runserver
```

### 5. Open in your browser
Go to: **http://127.0.0.1:8000**

---

## Project Structure

```
flagquiz/
├── manage.py               ← Run the server from here
├── requirements.txt        ← Python dependencies
├── flagquiz/               ← Project configuration
│   ├── settings.py         ← Django settings
│   └── urls.py             ← Root URL routing
└── quiz/                   ← Main application
    ├── flag_data.py        ← Country flag data (30 countries)
    ├── views.py            ← Page logic (home, quiz, answer, results)
    ├── urls.py             ← App URL routing
    ├── models.py           ← No models (sessions used instead)
    ├── templates/quiz/     ← HTML page templates
    │   ├── base.html       ← Shared header/footer layout
    │   ├── home.html       ← Main menu page
    │   ├── quiz.html       ← Question display page
    │   └── results.html    ← Final score page
    └── static/
        ├── css/style.css   ← All page styling
        └── js/quiz.js      ← Answer button feedback
```

---

## How It Works
1. User visits the home page and clicks **Start Quiz**
2. Django shuffles 30 flag questions and stores them in the session
3. Each question displays an emoji flag and 4 multiple-choice options
4. The user clicks an answer — JavaScript highlights correct/wrong instantly
5. Django checks the answer server-side, updates the score, and loads the next question
6. After all questions, the results page shows the final score and a message
