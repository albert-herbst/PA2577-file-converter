from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import requests
from flask_socketio import SocketIO, emit

# Load environment variables from .env file
load_dotenv()
CONVERTER_API = 'http://converter-service:8000'

# Create a Flask web server
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
socketio = SocketIO(app, cors_allowed_origins="*")

# Define a route and a function to handle it
@app.route('/')
def hello_world():
    return render_template('index.html')

# @app.route('/update_job', methods=['POST'])
# def update_job():
#     data = request.json
#     socketio.emit('job_progress', data)
#     return "Progress updated", 150

@app.route('/update_job', methods=['PATCH'])
def update_job():
    # Extract the job_id and progress from the incoming PATCH request
    data = request.get_json()
    job_id = data.get('job_id')
    progress = data.get('progress')

    # Emit the job progress update to all connected clients via WebSocket
    socketio.emit('job_progress', {'job_id': job_id, 'progress': progress})

    # Respond to the Converter Service to acknowledge the receipt of the update
    return jsonify({'message': f'Job {job_id} progress updated to {progress}%'}), 200


@socketio.on('connect')
def handle_connect():
    socketio.emit('update', "Client Connected")
    # requests.post(CONVERTER_API + '/convert', json={'job_id': 55})
    socketio.start_background_task(requests.post, CONVERTER_API + '/start_job', json={'job_id': 55})


# Run the app if this script is executed
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
