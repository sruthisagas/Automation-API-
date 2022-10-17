import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_get_download_link(self, auth_token_data):
        api_url = "https://some-URL/api/split/tunneling"
        access_token = auth_token_data
        print(access_token)
        assert access_token, "auth_token parameter should not be empty."
        for i in access_token:
            headers = {

                "authorization": i

            }
            body = {
                "app_name": "com.youtube.com",
                "action": "add"
            }

            print("\nauth token is:", i)
            r = requests.post(api_url, headers=headers, data=body)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            message = parsed_json["message"]
            print(status)
            if status == 201:
                print("Passed:  Download Links displayed successfully.")
            else:
                print("Failed: Download Links not displayed successfully", message)

        x = "carddev@sep27.com"
        y = "123456"
        user_id, auth_token, password_encrypted = test_for_auth_token.Test.test_for_auth_token(self, x, y)
        assert auth_token, "auth_token parameter should not be empty."
        header = {

            "authorization": auth_token

        }
        body = {
            "app_name": "com.youtube.com",
            "action": "add"
        }
        r = requests.post(api_url, headers=header, data=body)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        status = r.status_code
        message = parsed_json["message"]
        print(status)
        if status == 201:
            print("Passed: Download Links displayed successfully.")
        else:
            print("Failed:  Download Links not displayed successfully", message)








