import json
import requests


class Test:

    def test_get_clients(self):
        api_url = "https://some-URL/api/clients"
        r = requests.get(api_url)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        status = r.status_code
        print(status)
        if status == 201:
            print("Passed: Client list displayed successfully.")
        else:
            print("Failed: Client list not displayed successfully.")





