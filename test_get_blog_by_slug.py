import json
import requests


class Test:

    def test_get_blog_by_slug(self):
        api_url = "https://some-URL/api/blog/by/slug"
        params = {
            "catSlug": "streaming"
        }

        r = requests.get(api_url, params=params)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        status = r.status_code
        print(status)
        if status == 201:
            print("Passed: SwoshsVPN blog by slug displayed successfully.")
        else:
            print("Failed: SwoshsVPN blog by slug not displayed successfully.")





