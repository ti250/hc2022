
import veryfi
import pprint
import os
import requests

# Define authorisation info
CLIENT_ID = os.environ.get("CLIENT_ID")
ENVIRONMENT_URL = os.environ.get("ENVIRONMENT_URL")
username = os.environ.get("USER_NAME")
api_key = os.environ.get("API_KEY")


def get_receipt_info(image_path, file_name):

	# Auth
	process_file_url = '{0}api/v7/partner/documents/'.format(ENVIRONMENT_URL)
	headers = {
	    "Accept": "application/json",
	    "CLIENT-ID": CLIENT_ID,
	    "AUTHORIZATION": "apikey {0}:{1}".format(username, api_key)
	}

	# You can send the list of categories that is relevant to your case
	# Veryfi will try to choose the best one that fits this document
	categories = ["Office Expense", "Meals & Entertainment", "Utilities", "Automobile"]
	payload = {
	    'file_name': file_name,
	    'categories': categories
	}
	files = {'file': ('file', open(image_path, 'rb'), 'image/jpeg')}
	response = requests.post(url=process_file_url, headers=headers, data=payload, files=files)

	return response