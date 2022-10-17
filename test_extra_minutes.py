import json
import pytest
import requests

import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_extra_minutes(self, auth_token_data):
        api_url = "https://some-URL/api/extra_minutes"
        access_token = auth_token_data
        print(access_token)
        assert access_token, "auth_token parameter should not be empty."
        for i in access_token:
            headers = {

                "authorization": i

            }

            body = {
                "lang": "EN"
            }
            print("\nauth token is:", i)
            r = requests.post(api_url, data=body, headers=headers)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            message = parsed_json["message"]
            print(status)
            if status == 201 and message == "Start using your VPN connection.":
                print("Passed: Point redeemed successfully.")
            else:
                print("Failed: Point not redeemed.", message)

        user_name_data = ["carddev@sep27.com", "expire@test.com"]
        user_password_data = ["123456", "123456"]
        for x, y in zip(user_name_data, user_password_data):
            user_id, auth_token, password_encrypted = test_for_auth_token.Test.test_for_auth_token(self, x, y)
            assert auth_token, "auth_token parameter should not be empty."
            header = {

                "authorization": auth_token

            }
            body = {
                "lang": "EN"
            }
            print("auth token is:", auth_token)
            r = requests.post(api_url, data=body, headers=header)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            message = parsed_json["message"]
            print(status)
            if status == 201 and message == "Start using your VPN connection.":
                print("Passed: Point redeemed successfully.")
            else:
                print("Failed: Point not redeemed.", message)





