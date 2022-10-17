import json
import requests


class Test:

    def test_get_servers(self):
        api_url = "https://some-URL/api/servers"
        r = requests.get(api_url)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        status = r.status_code
        print(status)
        if status == 201:
            print("Passed: Servers and it's locations displayed successfully.")
        else:
            print("Failed: Servers and it's locations not displayed successfully.")





