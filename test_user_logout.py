import json
import unittest
import requests
import pytest

import test_for_auth_token
import test_user_login_password


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_user_logout(self, auth_token_data):
        logout_url = "https://some-URL/api/logout"
        access_token = auth_token_data
        print(access_token)
        assert access_token, "auth_token parameter should not be empty."
        for i in access_token:
            headers = {

                "authorization": i

            }
            print(i)

            r = requests.post(logout_url, headers=headers)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            print(r.status_code)
            if r.status_code == 201:
                print("Passed: User Logged out successfully.")
            else:
                print("Failed: User not Logged out.")

        user_name_data = "carddev@sep27.com"
        user_password_data = "123456"
        user_id, auth_token, password_encrypted = test_for_auth_token.Test.test_for_auth_token(self, user_name_data,

                                                                                               user_password_data)
        assert auth_token, "auth_token parameter should not be empty."
        header = {

            "authorization": auth_token

        }
        r = requests.post(logout_url, headers=header)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        print(r.status_code)
        if r.status_code == 201:
            print("Passed: User Logged out successfully.")
        else:
            print("Failed: User not Logged out.")


