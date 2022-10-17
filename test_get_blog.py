import json
import requests


class Test:

    def test_get_blog(self):
        api_url = "https://some-URL/api/blog"
        r = requests.get(api_url)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        status = r.status_code
        print(status)
        if status == 201:
            print("Passed: Blog record list displayed successfully.")
        else:
            print("Failed: Blog record list not displayed successfully.")





