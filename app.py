from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("message")
def handle_message(data):
    print(f"دریافت پیام: {data}")
    emit("response", {"message": f"پیام شما دریافت شد: {data}"}, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)
