from flask import Flask, send_from_directory, request
import json
import simplejson
import os
from server.process_supermarkets import PricesHelper
from server.receipt import get_receipt_info
from server.information_manager import InformationManager

app = Flask(__name__)
prices_helper = PricesHelper("server/super.csv")
information_manager = InformationManager(prices_helper.prices)
photo_index = 0


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


@app.route("/api/analyse_receipt", methods=["POST"])
def analyse_receipt():
    global photo_index
    photo = request.files["photo"]
    photo_file_name = f"received_receipt{photo_index % 10}.jpg"
    photo_index += 1
    photo_path = os.path.join("receipts", photo_file_name)
    photo.save(photo_path)

    receipt_info = get_receipt_info(photo_path, photo_file_name)
    receipt_name = receipt_info["vendor"]["name"]

    location_type = get_location_type(receipt_name)
    location_name = get_location_name(receipt_name)

    information_manager.add_reciept(receipt_info["line_items"], location_name)

    print(receipt_info)
    response = {
        "status": "success!",
        "locationType": location_type,
        "locationName": location_name
    }

    print(response)
    return response


def get_location_name(receipt_name):
    translation_dict = {
        "Sainsbury's": "Sainsbury's Local St Andrews St.",
        "Tesco": "Tesco Express Christs Lane",
        "Marks & Spencers": "M&S Sidney St.",
        "Waitrose": "Little Waitrose Fitzroy St."
    }
    if receipt_name in translation_dict:
        return translation_dict[receipt_name]
    else:
        return "Tesco Express Christs Lane"


def get_location_type(receipt_name):
    translation_dict = {
        "Sainsbury's": "sains",
        "Tesco": "tesco",
        "Marks & Spencers": "m&s",
        "Waitrose": "waitrose"
    }
    if receipt_name in translation_dict:
        return translation_dict[receipt_name]
    else:
        return "tesco"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
