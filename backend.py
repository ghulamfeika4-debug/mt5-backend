import json
import requests
from flask import Flask, request

# This is the "Receptionist" or "Public Backend" part
app = Flask(__name__)

@app.route("/receive_command", methods=["POST"])
def receive_command():
    try:
        data = request.json
        print("Received public command:", data)

        # The internal URL for your trading bot
        trading_bot_url = "http://127.0.0.1:5002/execute_trade"
        
        # Forward the command to the trading bot
        response = requests.post(trading_bot_url, json=data)
        
        # Get the response from the trading bot
        trading_bot_response = response.json()
        
        return json.dumps(trading_bot_response)

    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)})
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)