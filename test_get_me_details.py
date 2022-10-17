import json
import pytest
import requests

import test_for_auth_token
import test_user_login_password


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_get_me_details(self, auth_token_data):
        api_url = "https://some-URL/api/me"
        access_token = auth_token_data
        print(access_token)
        assert access_token, "auth_token parameter should not be empty."
        for i in access_token:
            headers = {

                "authorization": i

            }
            print("auth token is:", i)
            r = requests.get(api_url, headers=headers)
            print(r.status_code)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            if r.status_code == 201:
                print("Passed: User details found successfully.")
            else:
                print("Failed: User details not found successfully.")
        x = "carddev@sep27.com"
        y = "123456"
        user_id, auth_token, password_encrypted = test_for_auth_token.Test.test_for_auth_token(self, x, y)
        assert auth_token, "auth_token parameter should not be empty."

        headers = {

            "authorization": auth_token

        }

        r = requests.get(api_url, headers=headers)
        print(r.status_code)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        if r.status_code == 201:
            print("Passed: User details found successfully.")
        else:
            print("Failed: User details not found successfully.")



