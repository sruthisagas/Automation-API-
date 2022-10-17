import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_register_login_guest(self, auth_token_data):
        api_url = "https://some-URL/api/register_login_guest"
        body = {

            "device_code": "8A183C82-ABFB-4C53-A450-E34FA25C707C",
            "device_name": "Glaxy J3",
            "device_type": "android",
            "lang": "EN",
            "email": "fbli99jjx@tempmail.cn",
            "password": "123456"
        }

        r = requests.post(api_url, data=body)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        status = r.status_code
        message = parsed_json["message"]
        print(status)
        if status == 201:
            print("Passed: guest user registered & login successfully.")
        else:
            print("Failed: guest user not registered & login successfully.")





