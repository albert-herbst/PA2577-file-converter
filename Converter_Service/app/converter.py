from flask import Flask
import requests
import threading
import time

app = Flask(__name__)

# This function will simulate a long-running job that updates its progress every second.
def send_job_updates(job_id, update_url):
    progress = 0
    while progress < 100:
        progress += 5
        # Send a PATCH request to the Frontend Service with the current progress.
        requests.patch(update_url, json={'job_id': job_id, 'progress': progress})
        time.sleep(1)  # Wait for 1 second before sending the next update.

@app.route('/start_job')
def start_job(job_id):
    job_id = 10
    # Start the job update process in a background thread.
    update_url = 'http://frontend-service:8000/update_job'  # Replace with actual Frontend Service URL
    threading.Thread(target=send_job_updates, args=(job_id, update_url)).start()
    return f"Job {job_id} started", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Run on a different port than the Frontend Service.
