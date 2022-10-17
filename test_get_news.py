import json
import requests


class Test:

    def test_get_news(self):
        api_url = "https://some-URL/api/news"
        r = requests.get(api_url)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        status = r.status_code
        print(status)
        if status == 201:
            print("Passed: SwoshsVPN news list displayed successfully.")
        else:
            print("Failed: SwoshsVPN news not displayed successfully.")





