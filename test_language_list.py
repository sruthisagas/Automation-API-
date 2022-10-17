import json
import requests


class Test:

    def test_language_list(self):
        api_url = "https://some-URL/api/language"
        lang_list = ["en", "cn", "djshfdj", 23344]
        for i in lang_list:
            params = {
                "lang": i
            }
            r = requests.get(api_url, params=params)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            print(status)
            if status == 201:
                print("Passed: Language list displayed successfully.")
            else:
                print("Failed: Language list not displayed successfully.")
