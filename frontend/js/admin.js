
function setRisk() {
    // Random risk score (demo purpose)
    let risk = Math.floor(Math.random() * 101);

    const riskFill = document.getElementById("riskFill");
    const riskValue = document.getElementById("riskValue");

    riskValue.innerText = risk + "%";
    riskFill.style.width = risk + "%";

    // Risk color logic
    if (risk < 40) {
        riskFill.style.background = "green";
    } else if (risk < 70) {
        riskFill.style.background = "orange";
    } else {
        riskFill.style.background = "red";
    }
}

