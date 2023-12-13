from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import time
import random
import requests

# Load environment variables from .env file
load_dotenv()

FRONTEND_ENDPOINT = "http://frontend:5000"

# Create a Flask web server
app = Flask(__name__)

# Define a route and a function to handle it
@app.route('/')
def hello_world():
    # Render the HTML template
        return "Conversion Service"

@app.route('/convert', methods=['POST'])
def start_convert_job():
    duration = random.randint(4, 7)
    for i in range(21):
        time.sleep(duration/21)
        # Send progress update to frontend server
        requests.post(FRONTEND_ENDPOINT + '/update_job', json={'job_id': 55, 'progress': (5*i) })
    
    # Notify job completion
    requests.post(FRONTEND_ENDPOINT + '/job_complete', json={'job_id': 55})


# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
