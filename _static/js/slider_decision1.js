(function () {
    function getCurrentPage() {
        const url = window.location.pathname;
        if (url.includes("Decision_P0")) return 'P0';
        if (url.includes("Decision_P1")) return 'P1';
        if (url.includes("Decision_P2")) return 'P2';
        if (url.includes("Decision_P3")) return 'P3';
        if (url.includes("Decision_P4")) return 'P4';
        return null;
    }

    const currentPage = getCurrentPage();
    let slidername, thumbname;

    if (currentPage) {
        slidername = `id_decision_${currentPage}`;
        thumbname = `decision_${currentPage}`;
    } else {
        console.error('Unable to determine current page.');
        return;
    }

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
        thumbLabel.style.display = 'inline-block';
    }

    function revealOnInteraction(slider, thumbLabel, sustainableInput, conventionalInput) {
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

        revealOnInteraction(slider, thumbLabel, sustainableInput, conventionalInput);
        updateThumbLabel();
        updateConventionalFund(val);
    }

    function updateAllFromConventional(value) {
        const val = Math.min(100, Math.max(0, value));
        conventionalInput.value = val;
        sustainableInput.value = (100 - val).toFixed(0);
        slider.value = (100 - val);

        revealOnInteraction(slider, thumbLabel, sustainableInput, conventionalInput);
        updateThumbLabel();
        updateConventionalFund(100 - val);
    }

    function updateConventionalFund(sustainableValue) {
        const conventionalFund = document.getElementById('conventional_fund');
        conventionalFund.textContent = (100 - sustainableValue).toFixed(0);
    }

    let slider, sustainableInput, conventionalInput, thumbLabel;

    window.addEventListener('DOMContentLoaded', function () {
        slider = document.getElementById(slidername);
        sustainableInput = document.getElementById('input_sustainable');
        conventionalInput = document.getElementById('input_conventional');
        thumbLabel = document.getElementById(thumbname);

        if (!slider || !sustainableInput || !conventionalInput || !thumbLabel) {
            console.error("Missing one or more elements.");
            return;
        }

        const initialValue = parseFloat(slider.getAttribute('data-initial-value')) || 0;
        const sliderMax = parseFloat(slider.max) || 100;

        // Hide everything at start
        sustainableInput.value = '';
        conventionalInput.value = '';
        sustainableInput.style.color = 'transparent';
        conventionalInput.style.color = 'transparent';
        thumbLabel.style.display = 'none';
        thumbLabel.style.position = 'absolute';

        // Add or update the slider "last bar"
        let lastBar = document.querySelector('.slider-last-bar');
        if (!lastBar) {
            lastBar = document.createElement('div');
            lastBar.classList.add('slider-last-bar');
            slider.parentElement.appendChild(lastBar);
        }
        const lastBarPosition = 5 + (initialValue / sliderMax) * 90;
        lastBar.style.left = `${lastBarPosition.toFixed(2)}%`;

        // Event listeners
        slider.addEventListener('input', function () {
            const val = Math.max(0, Math.min(100, parseFloat(slider.value)));
            updateAllFromSustainable(val);
        });

        sustainableInput.addEventListener('input', function () {
            const val = parseFloat(sustainableInput.value);
            if (!isNaN(val)) updateAllFromSustainable(val);
        });

        conventionalInput.addEventListener('input', function () {
            const val = parseFloat(conventionalInput.value);
            if (!isNaN(val)) updateAllFromConventional(val);
        });
    });
})();
