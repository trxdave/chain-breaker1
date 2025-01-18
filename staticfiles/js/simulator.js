document.addEventListener("DOMContentLoaded", function () {
    console.log("Simulator.js loaded and DOMContentLoaded triggered!");

    const scenariosData = document.getElementById("scenarios-data");
    if (!scenariosData) {
        console.error("Scenarios data script not found!");
        return;
    }

    const scenarios = JSON.parse(scenariosData.textContent);
    console.log("Loaded Scenarios:", scenarios);

    let currentScenarioIndex = 0;

    // Load a scenario and its choices dynamically
    function loadScenario(index) {
        if (index >= scenarios.length) {
            console.error("Scenario index out of bounds:", index);
            return;
        }

        const scenario = scenarios[index];
        console.log("Loading scenario:", scenario);

        const scenarioDiv = document.getElementById("scenario");
        const choicesDiv = document.getElementById("choices");
        const feedbackDiv = document.getElementById("feedback");

        if (!scenarioDiv || !choicesDiv || !feedbackDiv) {
            console.error("One or more DOM elements are missing!");
            return;
        }

        feedbackDiv.style.display = 'none';
        scenarioDiv.innerHTML = `<p>${scenario.scenario}</p>`;
        choicesDiv.innerHTML = '';

        scenario.choices.forEach((choice, idx) => {
            const button = document.createElement("button");
            button.className = "btn btn-secondary m-2";
            button.textContent = choice;
            button.addEventListener("click", () => showFeedback(idx, scenario));
            choicesDiv.appendChild(button);
        });
    }

    // Show feedback after a choice is clicked
    function showFeedback(choiceIndex, scenario) {
        console.log(`User selected choice ${choiceIndex}:`, scenario.choices[choiceIndex]);

        const feedbackDiv = document.getElementById("feedback");
        const feedbackText = document.getElementById("feedback-text");
        const choicesDiv = document.getElementById("choices");

        feedbackText.textContent = `${scenario.feedback[choiceIndex]}\n\nKey Teaching Point: ${scenario.teachingPoint}`;
        feedbackDiv.style.display = 'block';
        choicesDiv.innerHTML = ''; // Clear choices after selection
    }

    // Handle "Next Scenario" button click
    document.getElementById("next-button").addEventListener("click", () => {
        currentScenarioIndex++;
        if (currentScenarioIndex < scenarios.length) {
            loadScenario(currentScenarioIndex);
        } else {
            document.getElementById("app").innerHTML = '<h2 class="text-center">Thank you for completing the simulator!</h2>';
        }
    });

    // Load the first scenario on page load
    loadScenario(currentScenarioIndex);
});
