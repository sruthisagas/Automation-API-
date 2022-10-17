import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_user_delete(self, auth_token_data):
        api_url = "https://some-URL/api/user/delete"
        access_token = auth_token_data
        print(access_token)
        assert access_token, "auth_token parameter should not be empty."
        for i in access_token:
            headers = {

                "authorization": i

            }

            body = {
                "password": "d7947f6d77c11b0f3cd8ead78660c6c3ffed709d03b0ba864172fa3a33aa8220",
                "reason": "for some reasons"
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

        x = "k8xp30d3c@tempmail.cn"
        y = "123456"
        user_id, auth_token, password_encrypted = test_for_auth_token.Test.test_for_auth_token(self, x, y)
        print(password_encrypted)
        assert auth_token, "auth_token parameter should not be empty."

        header = {

            "authorization": auth_token

        }
        body = {
            "password": "d7947f6d77c11b0f3cd8ead78660c6c3ffed709d03b0ba864172fa3a33aa8220",
            "reason": "for some reasons"
        }
        r = requests.post(api_url, data=body, headers=header)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        status = r.status_code
        message = parsed_json["message"]
        print(status)
        if status == 200:
            print("Passed: user deleted successfully.")
        else:
            print("Failed: Unable delete the user.", message)





