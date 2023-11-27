from flask import Flask, render_template
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Create a Flask web server
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Define a route and a function to handle it
@app.route('/')
def hello_world():
    # Render the HTML template
    return render_template('index.html')

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
