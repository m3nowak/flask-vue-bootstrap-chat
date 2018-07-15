from datetime import datetime

from flask import render_template, jsonify, request
from flask_socketio import SocketIO, send as socket_send

from custom_flask import Flask

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/api/send-msg", methods=["POST"])
def api_time():
    message_datetime = datetime.now()
    post_data = request.get_json()
    message_user = post_data['nick']
    message_content = post_data['message']
    broadcast_message = {
        'datetime': message_datetime.isoformat(),
        'user': message_user,
        'content': message_content,
    }
    socketio.emit('message', broadcast_message, json=True, broadcast=True)
    response_object = {'status': 'success'}
    return jsonify(response_object)