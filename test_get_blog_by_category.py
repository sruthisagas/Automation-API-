import json
import requests


class Test:

    def test_get_blog_by_category(self):
        api_url = "https://some-URL/api/blog/by/category"
        params = {
            "catSlug": "streaming"
        }
        r = requests.get(api_url, params=params)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        status = r.status_code
        print(status)
        if status == 201:
            print("Passed: SwoshsVPN blog by category displayed successfully.")
        else:
            print("Failed: SwoshsVPN blog by category not displayed successfully.")





