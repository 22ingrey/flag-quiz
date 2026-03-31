"""
flag_data.py
------------
Contains all country flag data used in the quiz.
Each entry includes the country name and its Unicode emoji flag.
Emoji flags work in all modern browsers without needing image files.

This module is imported by views.py to generate quiz questions.
"""

# List of dictionaries, each representing one quiz question.
# 'country' is the correct answer, 'flag' is the Unicode emoji flag.
FLAG_DATA = [
    {"country": "Australia",          "flag": "🇦🇺"},
    {"country": "Brazil",             "flag": "🇧🇷"},
    {"country": "Canada",             "flag": "🇨🇦"},
    {"country": "China",              "flag": "🇨🇳"},
    {"country": "Egypt",              "flag": "🇪🇬"},
    {"country": "France",             "flag": "🇫🇷"},
    {"country": "Germany",            "flag": "🇩🇪"},
    {"country": "India",              "flag": "🇮🇳"},
    {"country": "Indonesia",          "flag": "🇮🇩"},
    {"country": "Italy",              "flag": "🇮🇹"},
    {"country": "Japan",              "flag": "🇯🇵"},
    {"country": "Kenya",              "flag": "🇰🇪"},
    {"country": "Mexico",             "flag": "🇲🇽"},
    {"country": "New Zealand",        "flag": "🇳🇿"},
    {"country": "Nigeria",            "flag": "🇳🇬"},
    {"country": "Norway",             "flag": "🇳🇴"},
    {"country": "Pakistan",           "flag": "🇵🇰"},
    {"country": "Portugal",           "flag": "🇵🇹"},
    {"country": "Russia",             "flag": "🇷🇺"},
    {"country": "Saudi Arabia",       "flag": "🇸🇦"},
    {"country": "South Africa",       "flag": "🇿🇦"},
    {"country": "South Korea",        "flag": "🇰🇷"},
    {"country": "Spain",              "flag": "🇪🇸"},
    {"country": "Sweden",             "flag": "🇸🇪"},
    {"country": "Thailand",           "flag": "🇹🇭"},
    {"country": "Turkey",             "flag": "🇹🇷"},
    {"country": "United Kingdom",     "flag": "🇬🇧"},
    {"country": "United States",      "flag": "🇺🇸"},
    {"country": "Argentina",          "flag": "🇦🇷"},
    {"country": "Greece",             "flag": "🇬🇷"},
]
