from flask import Flask, send_from_directory, request
import json
import simplejson
from server.process_supermarkets import PricesHelper

app = Flask(__name__)
prices_helper = PricesHelper("server/super.csv")


# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route("/supermarketFavicons/<path:path>")
def get_supermarket_favicon(path):
    return send_from_directory('client/public/supermarketFavicons', path)


@app.route("/api/supermarket_recommendations", methods=["POST"])
def get_supermarket_recommendations():
    given_data = json.loads(request.data)
    quantities = given_data["quantities"]
    quantities = [{"name": quantity["name"].lower(), "quantity": quantity["quantity"]} for quantity in quantities]
    location = [given_data["location"]]
    recommendations = prices_helper.get_recommendations(location, quantities)
    print(recommendations)
    return simplejson.dumps({"recommendations": recommendations}, ignore_nan=True)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
