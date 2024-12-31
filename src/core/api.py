
from flask import Flask, jsonify, request
from typing import Dict, Any
import logging

class SentinelAPI:
    def __init__(self, sentinel_instance):
        self.app = Flask(__name__)
        self.sentinel = sentinel_instance
        self.logger = logging.getLogger('SentinelAPI')
        
        self.setup_routes()
        
    def setup_routes(self):
        @self.app.route('/api/status', methods=['GET'])
        def get_status():
            return jsonify({
                'status': 'active',
                'modules': len(self.sentinel.modules),
                'start_time': self.sentinel.start_time.isoformat()
            })
            
        @self.app.route('/api/modules', methods=['GET'])
        def get_modules():
            return jsonify([
                module.__class__.__name__ 
                for module in self.sentinel.modules
            ])
            
        @self.app.route('/api/execute', methods=['POST'])
        def execute_modules():
            try:
                self.sentinel.execute()
                return jsonify({'status': 'success'})
            except Exception as e:
                return jsonify({
                    'status': 'error',
                    'message': str(e)
                }), 500
                
    def run(self, host: str = '0.0.0.0', port: int = 5000):
        self.app.run(host=host, port=port)
