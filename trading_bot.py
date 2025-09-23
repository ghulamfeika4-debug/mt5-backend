import json
import MetaTrader5 as mt5
from flask import Flask, request

# This is the "Specialist" or "Trading Bot" part
app = Flask(__name__)

# This is the API endpoint that will receive commands
@app.route("/execute_trade", methods=["POST"])
def execute_trade():
    try:
        data = request.json
        print("Received command from backend:", data)

        # Your MetaTrader5 logic goes here
        # This is where you would initialize and send a trade request
        if not mt5.initialize():
            print("MT5 initialization failed")
            return json.dumps({"status": "error", "message": "MT5 initialization failed"})
        
        print("Executing trade based on descriptive data...")
        
        # Logic to translate the descriptive JSON into an MT5 command
        symbol = data.get("symbol")
        volume = data.get("volume")
        trade_type = data.get("type")

        # Example: check trade type
        if trade_type == "buy":
            print(f"Executing BUY order for {volume} lots of {symbol}")
            # mt5.buy(...)
            
        elif trade_type == "sell":
            print(f"Executing SELL order for {volume} lots of {symbol}")
            # mt5.sell(...)

        mt5.shutdown()
        
        return json.dumps({"status": "success", "message": "Trade executed"})
    except Exception as e:
        print(f"An error occurred: {e}")
        return json.dumps({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(port=5002) # This script will run on port 5002