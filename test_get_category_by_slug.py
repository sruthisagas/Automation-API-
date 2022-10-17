
import json
import requests


class Test:

    def test_get_category_by_slug(self):
        api_url = "https://some-URL/api/blog/by/slug"
        for i in ["feature", "digital-security-lab" , "streaming", "tips-tricks"]:

            params = {
                "slug": i
            }
            print("category is:", i)
            r = requests.get(api_url, params=params)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            print(status)
            if status == 201:
                print("Passed: SwoshsVPN category by slug displayed successfully.")
            else:
                print("Failed: SwoshsVPN category by slug not displayed successfully.")





