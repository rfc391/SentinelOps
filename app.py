
from src.web import app
from src.sockets import socketio

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=3000)
