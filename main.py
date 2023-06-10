from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, leave_room, SocketIO, send
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] = "27eR0/iGMMojTBKCGeNQp7O4zZ6pyG13pAWub4bhjK8="
socketio = SocketIO(app)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


if __name__ == "__main__":
    socketio.run(app, debug=True, host='127.0.0.1', port='8000')
