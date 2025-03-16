var socket = io("http://localhost:5000");

socket.on("response", function(data) {
    let li = document.createElement("li");
    li.textContent = data.message;
    document.getElementById("messages").appendChild(li);
});

function sendMessage() {
    let message = document.getElementById("message").value;
    socket.emit("message", message);
    document.getElementById("message").value = "";
}