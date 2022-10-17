import json
import requests


class Test:

    def test_get_version(self):
        api_url = "https://some-URL/api/version"
        r = requests.get(api_url)
        print(r.status_code)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        if r.status_code == 201:
            print("Passed: Version details got successfully.")
        else:
            print("Failed: Version details not received.")



