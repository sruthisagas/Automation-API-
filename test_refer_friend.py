import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_refer_friend(self, auth_token_data):
        api_url = "https://some-URL/api/refer/friend"
        access_token = auth_token_data
        print(access_token)
        assert access_token, "auth_token parameter should not be empty."
        for i in access_token:
            headers = {

                "authorization": i

            }

            body = {
                "email": "john@example.com",
                "lang": "EN"
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
        user_name_data = ["carddev@sep27.com", "expire@test.com", "testmon@gmail.com"]
        for j in user_name_data:

            header = {

                "authorization": auth_token

            }
            body = {
                "email": j,
                "lang": "EN"
            }
            print("auth token is:", auth_token)
            r = requests.post(api_url, data=body, headers=header)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            message = parsed_json["message"]
            print(status)
            if status == 201:
                print("Passed: Message sent successfully.")
            else:
                print("Failed: Message not sent successfully.", message)





