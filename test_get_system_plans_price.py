import json
import requests


class Test:

    def test_get_user_shortcut_links(self):
        api_url = "https://some-URL/api/systemplans/price"
        r = requests.get(api_url)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        status = r.status_code
        print(status)
        if status == 201:
            print("Passed: System plan prices displayed successfully.")
        else:
            print("Failed: System plan prices not displayed successfully.")





