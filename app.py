
from flask import Flask, jsonify
from flask_socketio import SocketIO
from src.core.sentinel import Sentinel
from src.modules.analytics import Analytics
from src.modules.security_manager import SecurityManager
from src.modules.operations_tracker import OperationsTracker

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sentinelops-secret-key'
socketio = SocketIO(app)

sentinel = Sentinel(name="SentinelOps Web Instance")
analytics = Analytics()
security = SecurityManager()
ops_tracker = OperationsTracker()

sentinel.register_module(analytics)
sentinel.register_module(security)
sentinel.register_module(ops_tracker)

@app.route('/')
def index():
    return 'SentinelOps is running'

@app.route('/api/metrics')
def get_metrics():
    return jsonify({
        'operations': ops_tracker.get_metrics(),
        'start_time': sentinel.start_time.isoformat()
    })

@app.route('/api/events')
def get_events():
    return jsonify({
        'events': ops_tracker.get_events()
    })

@app.route('/api/status')
def get_status():
    return jsonify({
        'status': 'active',
        'modules': [m.__class__.__name__ for m in sentinel.modules],
        'uptime': str(datetime.now() - sentinel.start_time)
    })

if __name__ == '__main__':
    sentinel.execute()
    socketio.run(app, debug=True, host='0.0.0.0', port=3000)
