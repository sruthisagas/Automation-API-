import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_visitor(self):

        api_url = 'https://apidev.swoshstest.com/api/software-download-logs'
        body = {
            "page": "example.com/xyz",
            "referrer": "google.com",
            "date": "2022-08-15",
            "useragent": "xyz",
            "user_ip": "192.168.1.1"
            }
        r = requests.post(api_url, data=body)
        print(r.status_code)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        if r.status_code == 201:
            print("Passed:  Saved visitor details as expected.")
        else:
            print("Failed:  Saved visitor details not displayed as expected.")
