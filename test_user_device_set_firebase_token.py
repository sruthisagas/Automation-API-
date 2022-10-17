import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_user_device_set_firebase_token(self, auth_token_data):
        api_url = "https://some-URL/api/user/device/set/firebase/token"
        access_token = auth_token_data
        print(access_token)
        assert access_token, "auth_token parameter should not be empty."
        for i in access_token:
            headers = {

                "authorization": i

            }

            body = {
                "firebase_token": "c2aK9KHmw8E:APA91bF7MY9bNnvGAXgbHN58lyDxc9KnuXNXwsqUs4uV4GyeF06HM1hMm-etu63S_4C-G"
            }
            print("\nauth token is:", i)
            r = requests.post(api_url, data=body, headers=headers)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            message = parsed_json["message"]
            print(status)
            if status == 201:
                print("Passed: Message sent successfully.")
            else:
                print("Failed: Message not sent successfully.", message)

        x = "carddev@sep27.com"
        y = "123456"
        user_id, auth_token, password_encrypted = test_for_auth_token.Test.test_for_auth_token(self, x, y)
        assert auth_token, "auth_token parameter should not be empty."

        header = {

            "authorization": auth_token

        }
        body = {
            "firebase_token": "c2aK9KHmw8E:APA91bF7MY9bNnvGAXgbHN58lyDxc9KnuXNXwsqUs4uV4GyeF06HM1hMm-etu63S_4C-G"
        }
        r = requests.post(api_url, data=body, headers=header)
        status = r.status_code
        print(status)
        if status == 201:
            print("Passed: update user device firebase token for push notification.")
        else:
            print("Failed: user device firebase token is not updated for push notification")





