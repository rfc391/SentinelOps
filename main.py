
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
from datetime import datetime
from src.core.sentinel import Sentinel
from src.modules.analytics import Analytics
from src.modules.security_manager import SecurityManager
from src.modules.operations_tracker import OperationsTracker

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sentinelops-secret'
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
    return render_template('index.html')

@app.route('/api/status')
def get_status():
    return jsonify({
        'status': 'active',
        'modules': [m.__class__.__name__ for m in sentinel.modules],
        'uptime': str(datetime.now() - sentinel.start_time),
        'device_optimized': True
    })

@app.route('/api/metrics')
def get_metrics():
    return jsonify({
        'operations': ops_tracker.get_metrics(),
        'insights': analytics.get_insights(),
        'start_time': sentinel.start_time.isoformat()
    })

if __name__ == '__main__':
    sentinel.execute()
    socketio.run(app, debug=True, host='0.0.0.0', port=3000)
