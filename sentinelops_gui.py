
# Adding a GUI to the SentinelOps project for cross-platform usability
# Since PyQt5 is unavailable, we switch to a pure HTML-based local server approach using Flask.

from flask import Flask, render_template, request, jsonify
import os
import subprocess
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_sentinel_ops():
    data = request.json
    directory = data.get('directory')

    if not os.path.isdir(directory):
        return jsonify({"status": "error", "message": "Invalid directory."})

    try:
        process = subprocess.Popen(
            ["python", "sentinelops.py"], cwd=directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()

        return jsonify({
            "status": "success",
            "stdout": stdout.decode() if stdout else "",
            "stderr": stderr.decode() if stderr else ""
        })
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "sentinelops.py not found in the specified directory."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/clear', methods=['POST'])
def clear_logs():
    return jsonify({"status": "success", "message": "Logs cleared."})

if __name__ == "__main__":
    try:
        # Attempt to bind to port 5001; fallback to other ports if necessary
        app.run(host="127.0.0.1", port=5001, debug=True)
    except OSError as e:
        if "Address already in use" in str(e):
            sys.stderr.write("Port 5001 is in use. Trying port 5002.\n")
            try:
                app.run(host="127.0.0.1", port=5002, debug=True)
            except OSError as inner_e:
                sys.stderr.write("Port 5002 is also in use. Trying port 5003.\n")
                try:
                    app.run(host="127.0.0.1", port=5003, debug=True)
                except Exception as final_e:
                    sys.stderr.write(f"Error starting the Flask application on port 5003: {final_e}\n")
                    sys.exit(1)
            except Exception as inner_e:
                sys.stderr.write(f"Error starting the Flask application on port 5002: {inner_e}\n")
                sys.exit(1)
        else:
            sys.stderr.write(f"Port binding error: {e}\n")
            sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"Error starting the Flask application: {e}\n")
        sys.exit(1)
