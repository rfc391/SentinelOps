from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    emit('message', {'data': 'Connected to SentinelOps WebSocket!'})

def send_alert(message):
    socketio.emit('alert', {'message': message})
