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
        scenarioList.innerHTML = ""; // Clear existing content
    
        const row1 = document.createElement("div");
        row1.className = "row justify-content-center mb-4";
        
        const row2 = document.createElement("div");
        row2.className = "row justify-content-center";
    
        scenarios.forEach((scenario, index) => {
            const col = document.createElement("div");
            col.className = "col-md-4 mb-4 d-flex justify-content-center";
            col.innerHTML = `
                <img 
                    src="/static/images/scenario-${index + 1}.jpg" 
                    alt="Scenario ${index + 1}" 
                    class="img-fluid scenario-image" 
                    data-scenario-index="${index}"
                >
            `;
    
            col.querySelector('img').addEventListener("click", () => showScenario(index));
            
            // Add first 3 to row1, rest to row2
            if (index < 3) {
                row1.appendChild(col);
            } else {
                row2.appendChild(col);
            }
        });
    
        scenarioList.appendChild(row1);
        scenarioList.appendChild(row2);
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
