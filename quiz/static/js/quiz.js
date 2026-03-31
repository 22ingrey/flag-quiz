// quiz.js - Handles answer button feedback on the quiz page

// Wait for the page to fully load before running any code
document.addEventListener('DOMContentLoaded', function() {

    // Get all the answer buttons on the page
    var buttons = document.querySelectorAll('.choice-btn');

    // Get the correct answer from the hidden form field
    var correctAnswer = document.querySelector('input[name="correct_answer"]').value;

    // Loop through each button and add a click event
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', function(event) {
            event.preventDefault();

            var selected = this.value;

            // Disable all buttons so the user can't click again
            for (var j = 0; j < buttons.length; j++) {
                buttons[j].disabled = true;
            }

            // Check if the selected answer is correct or wrong
            if (selected === correctAnswer) {
                this.classList.add('correct');
            } else {
                // Mark selected button as wrong
                this.classList.add('wrong');
                // Show which one was correct
                for (var k = 0; k < buttons.length; k++) {
                    if (buttons[k].value === correctAnswer) {
                        buttons[k].classList.add('correct');
                    }
                }
            }

            // Submit the form after a short delay so the user can see the feedback
            var form = document.getElementById('answer-form');
            var hiddenInput = document.createElement('input');
            hiddenInput.type = 'hidden';
            hiddenInput.name = 'selected_answer';
            hiddenInput.value = selected;
            form.appendChild(hiddenInput);

            setTimeout(function() {
                form.submit();
            }, 1000);
        });
    }

});
