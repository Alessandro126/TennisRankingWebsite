document.addEventListener("DOMContentLoaded", function () {
    // Simulated ranking data (replace with real data from Python)
    const ranking = [
        ["Pietro"],
        ["Alessandro", "Neo"],
        ["Matteo", "Iwen"],
        ["Noel", "a", "b", "c"],
        ["d", "ef", "g", "h", "Iwen"],
        ["j", "k", "l", "Matteo", "n", "o"],
        ["p"]
    ];

    const pyramid = document.getElementById("pyramid");

    ranking.forEach(rowPlayers => {
        const row = document.createElement("div");
        row.classList.add("row");

        rowPlayers.forEach(player => {
            const box = document.createElement("div");
            box.classList.add("player-box");
            box.textContent = player;
            row.appendChild(box);
        });

        pyramid.appendChild(row);
    });
});
