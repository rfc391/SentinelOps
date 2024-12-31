
from flask import Flask
from flask_socketio import SocketIO
from src.core.sentinel import Sentinel
from src.modules.analytics import Analytics
from src.modules.security_manager import SecurityManager
from src.modules.operations_tracker import OperationsTracker

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sentinelops-secret-key'
socketio = SocketIO(app)

sentinel = Sentinel(name="SentinelOps Web Instance")
sentinel.register_module(Analytics())
sentinel.register_module(SecurityManager())
sentinel.register_module(OperationsTracker())

@app.route('/')
def index():
    return 'SentinelOps is running'

if __name__ == '__main__':
    sentinel.execute()
    socketio.run(app, debug=True, host='0.0.0.0', port=3000)
