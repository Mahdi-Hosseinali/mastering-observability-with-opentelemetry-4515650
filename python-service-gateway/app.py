from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

toggle = 0

blue_url = os.getenv('SERVICE_BLUE', 'http://localhost:3020')
green_url = os.getenv('SERVICE_GREEN', 'http://localhost:3010')

@app.route('/')
def index():
    global toggle
    choice = request.args.get('choice', '')
    url = f"{green_url if toggle < 3 else blue_url}?choice={choice}"

    try:
        response = requests.get(url)
        # Increment or reset the toggle based on its current value
        toggle = toggle + 1 if toggle < 3 else 0
        if response.status_code > 299:
            # If there is an error with the request, respond with the error
            return jsonify(error='Something went wrong!'), response.status_code
        # Return the JSON response from the request
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle connection errors
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
