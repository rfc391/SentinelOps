
from flask import Flask
from flask_socketio import SocketIO
from src.web import app
from src.core.sentinel import Sentinel

sentinel = Sentinel(name="SentinelOps Web Instance")
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=3000)
