
document.addEventListener("DOMContentLoaded", function () {
    if (!window.scheduleResults || window.scheduleResults.length === 0) return;

    let results = window.scheduleResults;
    let currentIndex = 0;

    const scheduleBox = document.querySelector("#schedule-box");
    const scheduleDisplay = document.querySelector("#schedule-display");
    const prevBtn = document.querySelector("#prev-btn");
    const nextBtn = document.querySelector("#next-btn");

    function updateScheduleDisplay() {
        if (results.length > 0) {
            scheduleDisplay.innerHTML = Object.entries(results[currentIndex])
                .map(([period, className]) => `<p>Period ${period}: ${className}</p>`)
                .join("");
            scheduleBox.style.display = "block";
        }
    }
    prevBtn.addEventListener("click", function () {
        if (currentIndex > 0) {
            currentIndex--;
            updateScheduleDisplay();
        }
    });
    nextBtn.addEventListener("click", function () {
        if (currentIndex < results.length - 1) {
            currentIndex++;
            updateScheduleDisplay();
        }
    });

    updateScheduleDisplay();
});




