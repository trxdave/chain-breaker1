document.addEventListener("DOMContentLoaded", function () {
    console.log("Simulator.js loaded and DOMContentLoaded triggered!");

    const scenariosData = document.getElementById("scenarios-data");
    if (!scenariosData) {
        console.error("Scenarios data script not found!");
        return;
    }

    const scenarios = JSON.parse(scenariosData.textContent);
    console.log("Loaded Scenarios:", scenarios);

    let currentScenarioIndex = null;

    const dashboard = document.getElementById("dashboard");
    const scenarioView = document.getElementById("scenario-view");
    const scenarioDiv = document.getElementById("scenario");
    const choicesDiv = document.getElementById("choices");
    const feedbackDiv = document.getElementById("feedback");
    const backButton = document.getElementById("back-button");
    const scenarioList = document.getElementById("scenario-list");

    if (!dashboard || !scenarioView || !scenarioDiv || !choicesDiv || !feedbackDiv || !backButton || !scenarioList) {
        console.error("One or more required DOM elements are missing!");
        return;
    }

    function showDashboard() {
        dashboard.style.display = "block";
        scenarioView.style.display = "none";
        scenarioList.innerHTML = "";
    
        scenarios.forEach((scenario, index) => {
            const card = document.createElement("div");
            card.className = "col-md-6 mb-4 scenario-card";
            card.innerHTML = `
                <img 
                    src="/static/images/scenario-${index + 1}.jpg" 
                    alt="Scenario ${index + 1}" 
                    class="img-fluid scenario-image" 
                    data-scenario-index="${index}"
                >
            `;
    
            card.querySelector('img').addEventListener("click", () => showScenario(index));
            scenarioList.appendChild(card);
        });
    }
    

    function showScenario(index) {
        currentScenarioIndex = index;
        const scenario = scenarios[index];

        dashboard.style.display = "none";
        scenarioView.style.display = "block";

        scenarioDiv.innerHTML = `
            <h2>Scenario ${index + 1}</h2>
            <p>${scenario.scenario}</p>
        `;

        choicesDiv.innerHTML = "";
        choicesDiv.style.display = "block"; // Ensure choices are visible
        scenario.choices.forEach((choice, idx) => {
            const button = document.createElement("button");
            button.className = "btn btn-secondary m-2";
            button.textContent = choice;
            button.addEventListener("click", () => showFeedback(idx, scenario));
            choicesDiv.appendChild(button);
        });

        feedbackDiv.style.display = "none";
    }

    function showFeedback(choiceIndex, scenario) {
        feedbackDiv.style.display = "block";
        feedbackDiv.innerHTML = `
            <p id="feedback-text">${scenario.feedback[choiceIndex]}</p>
            <p><strong>Key Teaching Point:</strong> ${scenario.teachingPoint}</p>
        `;
        choicesDiv.style.display = "none";
        scenarioDiv.style.display = "block"; // Keep scenario visible
    }

    backButton.addEventListener("click", showDashboard);

    showDashboard();
});
