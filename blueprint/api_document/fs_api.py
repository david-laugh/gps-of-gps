import json

import requests


def execute():
	url = "https://api.foursquare.com/v3/places/search"

	params = {
		"query": "coffee",
		"ll": "47.606,-122.349358",
		"open_now": "true",
		"sort":"DISTANCE"
	}
	headers = {
		"Accept": "application/json",
		"Authorization": "Your API KEY"
	}

	response = requests.request("GET", url, params=params, headers=headers)

	with open('sample.json', 'w', encoding="utf-8") as f:
		json.dump(response.json(), f, ensure_ascii=False)


if __name__=="__main__":
	execute()
