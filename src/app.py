
from datetime import datetime
from flask import Flask, jsonify
from flask_socketio import SocketIO
from typing import Dict, List

from src.core.sentinel import Sentinel
from src.modules.analytics import Analytics
from src.modules.security_manager import SecurityManager
from src.modules.operations_tracker import OperationsTracker
from src.modules.alert_manager import AlertManager
from src.modules.rate_limiter import RateLimiter
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'

rate_limiter = RateLimiter()
alert_manager = AlertManager()

def rate_limit(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        key = request.remote_addr
        allowed, wait_time = rate_limiter.is_allowed(key)
        if not allowed:
            return jsonify({
                "error": "Rate limit exceeded",
                "wait_seconds": wait_time
            }), 429
        return f(*args, **kwargs)
    return decorated_function
app.config['SECRET_KEY'] = 'sentinelops-secret-key'
socketio = SocketIO(app)

# Initialize core components
sentinel = Sentinel(name="SentinelOps Web Instance")
analytics = Analytics()
security = SecurityManager()
ops_tracker = OperationsTracker()

# Register modules
for module in [analytics, security, ops_tracker]:
    sentinel.register_module(module)

@app.route('/')
def index() -> str:
    return render_template('dashboard.html')

@app.route('/api/metrics')
def get_metrics() -> Dict:
    return jsonify({
        'operations': ops_tracker.get_metrics(),
        'start_time': sentinel.start_time.isoformat()
    })

@app.route('/api/events')
def get_events() -> Dict:
    return jsonify({
        'events': ops_tracker.get_events()
    })

@app.route('/api/status')
def get_status() -> Dict:
    return jsonify({
        'status': 'active',
        'modules': [m.__class__.__name__ for m in sentinel.modules],
        'uptime': str(datetime.now() - sentinel.start_time),
        'device_optimized': True,
        'mobile_ready': True
    })

@app.route('/api/mobile/summary')
def get_mobile_summary() -> Dict:
    """Lightweight endpoint for mobile devices"""
    return jsonify({
        'status': 'active',
        'alert_count': len(ops_tracker.get_events()),
        'last_update': datetime.now().isoformat()
    })

if __name__ == '__main__':
    sentinel.execute()
    socketio.run(app, debug=True, host='0.0.0.0', port=3000)
