document.addEventListener('DOMContentLoaded', function() {
    let pages = document.querySelectorAll('.instruction-page');
    let currentPageIndex = 0;
    let form = document.querySelector('#form');
    let nextButton = document.querySelector('#next-button');
    let prevButton = document.querySelector('#prev-button');

    let visitedPages = new Array(pages.length).fill(false);

    // Initialize the first page as active
    pages[currentPageIndex].classList.add('active');
    showCurrentPage();
    updateNextButtonText();

    function updateNextButtonText() {
        nextButton.innerText = "Next Page";
        if (currentPageIndex === pages.length - 1) {
        }

        if (currentPageIndex === 0) {
            prevButton.style.visibility = 'hidden';
        } else {
            prevButton.style.visibility = 'visible';
        }
    }

    function checkUnansweredQuestionsOnPage(pageIndex) {
        var questions = pages[pageIndex].querySelectorAll(".question");
        for (var i = 0; i < questions.length; i++) {
            var inputs = questions[i].getElementsByTagName("input");
            var answered = false;
            for (var j = 0; j < inputs.length; j++) {
                if (inputs[j].type === "radio" && inputs[j].checked) {
                    answered = true;
                    break;
                }
            }
            if (!answered) {
                return false;
            }
        }
        return true;
    }

    function checkSliderInteraction(pageIndex) {
        const sliders = pages[pageIndex].querySelectorAll(".custom-slider");
        for (let i = 0; i < sliders.length; i++) {
            const slider = sliders[i];
            // Check if the slider has been interacted with
            if (!slider.classList.contains('myclass1')) {
                return false; // If any slider hasn't been interacted with, return false
            }
        }
        return true; // All sliders have been interacted with
    }


    function checkAnswersCorrectOnPage(pageIndex) {
    var questions = pages[pageIndex].querySelectorAll(".question");
    for (var i = 0; i < questions.length; i++) {
        var correctAnswer = questions[i].dataset.correctAnswer; // Assuming correct answers are stored in a `data-correct-answer` attribute
        var inputs = questions[i].getElementsByTagName("input");
        var answeredCorrectly = false;
        for (var j = 0; j < inputs.length; j++) {
            if (inputs[j].type === "radio" && inputs[j].checked && inputs[j].value === correctAnswer) {
                answeredCorrectly = true;
                break;
            }
        }
        if (!answeredCorrectly) {
            return false;
        }
    }
    return true;
}

    function checkEstimationInputs(pageIndex) {
        let estCon2 = pages[pageIndex].querySelector("#est_con_2");
        let estSus2 = pages[pageIndex].querySelector("#est_sus_2");
        let estCon3 = pages[pageIndex].querySelector("#est_con_3");
        let estSus3 = pages[pageIndex].querySelector("#est_sus_3");

        let inputs = [estCon2, estSus2, estCon3, estSus3]; // Store in an array

        for (let input of inputs) {
            if (input && input.value.trim() === "") { // Check if input exists and is empty
                alert("Please enter all required estimations before proceeding.");
                return false;
            }
        }
        return true;
    }

    function showCurrentPage() {
        pages.forEach((page, index) => {
            page.classList.toggle('active', index === currentPageIndex);
        });

    //     // hide the next button on the most informative page for 5 seconds
    //     if (currentPageIndex === 2) {
    //         if (!visitedPages[currentPageIndex]) {
    //             nextButton.style.display = 'none';
    //             setTimeout(() => {
    //                 nextButton.style.display = 'inline-block';
    //                 visitedPages[currentPageIndex] = true;
    //             }, 10000);
    //         } else {
    //             nextButton.style.display = 'inline-block';
    //         }
    //     } else {
    //         nextButton.style.display = 'inline-block';
    //     }
    }

    function nextPage() {
        if (!checkUnansweredQuestionsOnPage(currentPageIndex)) {
            alert("Please answer all questions on this page before proceeding.");
            return;
        }
        if (!checkSliderInteraction(currentPageIndex)) {
            alert("Please interact with the slider on this page before proceeding.");
            return;
        }
        if (!checkAnswersCorrectOnPage(currentPageIndex)) {
            alert("One or more of your answers are incorrect. Please review and try again.");
            return;
        }
        if (!checkEstimationInputs(currentPageIndex)) {
            return;
        }

        if (currentPageIndex < pages.length - 1) {
            pages[currentPageIndex].classList.remove('active');
            currentPageIndex++;
            pages[currentPageIndex].classList.add('active');
            showCurrentPage();
            updateNextButtonText();
        } else {
            form.submit();
        }
    }

    function prevPage() {
        if (currentPageIndex > 0) {
            pages[currentPageIndex].classList.remove('active');
            currentPageIndex--;
            pages[currentPageIndex].classList.add('active');
            showCurrentPage();
            updateNextButtonText();
        }
    }


    prevButton.addEventListener('click', prevPage);
    nextButton.addEventListener('click', nextPage);
    updateNextButtonText();  // Initialize button text
});