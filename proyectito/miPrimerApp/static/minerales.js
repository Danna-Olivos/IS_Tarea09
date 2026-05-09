const colores = ["#e74c3c", "#2ecc71", "#3498db", "#f39c12", "#9b59b6"];

function cambiarColor() {
    const indice = Math.floor(Math.random() * colores.length);
    document.body.style.backgroundColor = colores[indice];
}