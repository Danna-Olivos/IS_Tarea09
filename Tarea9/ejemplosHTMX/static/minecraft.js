const mensajes = [
    "☀️ El Creeper explota en 3... 2... 1...",
    "💎 ¡Encontraste diamantes en la capa 12!",
    "🌙 Consejo: nunca caves directo hacia abajo",
    "⚔️ Un Enderman te está mirando fijamente...",
    "🏠 Recuerda construir tu casa antes de que anochezca",
    "🧟 Un zombie golpea tu puerta de madera",
];

function mensajeAleatorio() {
    const indice = Math.floor(Math.random() * mensajes.length);
    alert(mensajes[indice]);
}