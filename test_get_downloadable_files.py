import json
import pytest
import requests


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_get_downloadable_files(self, auth_token_data):
        api_url = "https://some-URL/api/get/downloadable/files/link"
        r = requests.get(api_url)
        print(r.status_code)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        if r.status_code == 201:
            print("Passed: Downloadable files link displayed successfully.")
        else:
            print("Failed: Downloadable files link not found.")



