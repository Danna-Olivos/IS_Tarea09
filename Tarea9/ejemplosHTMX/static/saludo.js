let clicks = 0;

function contarClicks() {
    clicks++;
    document.getElementById("contador").textContent = "Has hecho clic " + clicks + " veces";
}