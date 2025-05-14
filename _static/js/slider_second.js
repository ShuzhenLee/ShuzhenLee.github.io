(function() {
    const slidername = 'id_second_allocation';
    const thumbname = 'second_allocation';

    function updateThumbLabel() {
        const slider = document.getElementById(slidername);
        const thumbLabel = document.getElementById(thumbname);
        const sliderValue = parseFloat(slider.value);

        thumbLabel.textContent = `
        Conventional fund: ${(100 - sliderValue).toFixed(0)}%;
        Sustainable fund: ${sliderValue.toFixed(0)}%`;

        const thumbPosition = ((sliderValue - slider.min) / (slider.max - slider.min)) * 100;
        thumbLabel.style.left = `${thumbPosition}%`;
        thumbLabel.style.transform = `translate(-50%)`;
        thumbLabel.style.display = 'inline-block'; // show when updated
    }

    function revealInputsAndLabel() {
        slider.classList.add('myclass1');
        thumbLabel.style.display = 'inline-block';
        sustainableInput.style.color = '#000';
        conventionalInput.style.color = '#000';
    }

    function updateAllFromSustainable(value) {
        const val = Math.min(100, Math.max(0, value));
        sustainableInput.value = val;
        conventionalInput.value = (100 - val).toFixed(0);
        slider.value = val;

        revealInputsAndLabel();
        updateThumbLabel();
        checkEnableButton();
    }

    function updateAllFromConventional(value) {
        const val = Math.min(100, Math.max(0, value));
        conventionalInput.value = val;
        sustainableInput.value = (100 - val).toFixed(0);
        slider.value = (100 - val);

        revealInputsAndLabel();
        updateThumbLabel();
        checkEnableButton();
    }

    function checkEnableButton() {
        const sVal = parseFloat(sustainableInput.value);
        const cVal = parseFloat(conventionalInput.value);
        const valid = (
            !isNaN(sVal) && !isNaN(cVal) &&
            sVal >= 0 && sVal <= 100 &&
            cVal >= 0 && cVal <= 100 &&
            Math.abs(sVal + cVal - 100) < 0.01
        );
        nextButton.disabled = !valid;
    }

    let slider, sustainableInput, conventionalInput, nextButton, thumbLabel;

    window.addEventListener('DOMContentLoaded', function () {
        slider = document.getElementById(slidername);
        sustainableInput = document.getElementById('input_sustainable');
        conventionalInput = document.getElementById('input_conventional');
        nextButton = document.getElementById('next-button');
        thumbLabel = document.getElementById(thumbname);

        if (!slider || !sustainableInput || !conventionalInput || !nextButton || !thumbLabel) {
            console.error("Missing one or more elements (slider, inputs, button, or thumb label).");
            return;
        }

        // Hide thumb label and inputs initially
        thumbLabel.style.display = 'none';
        thumbLabel.style.position = 'absolute';
        sustainableInput.value = '';
        conventionalInput.value = '';
        sustainableInput.style.color = 'transparent';
        conventionalInput.style.color = 'transparent';

        // Slider changes
        slider.addEventListener('input', function () {
            const val = parseFloat(slider.value);
            updateAllFromSustainable(val);
        });

        // Sustainable input changes
        sustainableInput.addEventListener('input', function () {
            const val = parseFloat(sustainableInput.value);
            if (!isNaN(val)) {
                updateAllFromSustainable(val);
            }
        });

        // Conventional input changes
        conventionalInput.addEventListener('input', function () {
            const val = parseFloat(conventionalInput.value);
            if (!isNaN(val)) {
                updateAllFromConventional(val);
            }
        });
    });
})();
