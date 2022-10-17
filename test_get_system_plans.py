import json
import requests


class Test:

    def test_get_system_plans(self):
        api_url = "https://some-URL/api/systemplans"
        r = requests.get(api_url)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        status = r.status_code
        print(status)
        if status == 201:
            print("Passed: System plans displayed successfully.")
        else:
            print("Failed: System plans not displayed successfully.")





