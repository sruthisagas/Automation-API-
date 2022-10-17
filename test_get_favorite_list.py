import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_get_favorite_list(self, auth_token_data):
        api_url = "https://some-URL/api/favorite/list"
        access_token = auth_token_data
        print(access_token)
        assert access_token, "auth_token parameter should not be empty."
        for i in access_token:
            headers = {

                "authorization": i

            }
            print("\nauth token is:", i)
            r = requests.get(api_url, headers=headers)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            message = parsed_json["message"]
            print(status)
            if status == 201:
                print("Passed:  Favorite lists displayed successfully.")
            else:
                print("Failed:  Favorite lists not displayed successfully", message)

        x = "carddev@sep27.com"
        y = "123456"
        user_id, auth_token, password_encrypted = test_for_auth_token.Test.test_for_auth_token(self, x, y)
        assert auth_token, "auth_token parameter should not be empty."

        header = {

            "authorization": auth_token

        }
        r = requests.get(api_url, headers=header)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        status = r.status_code
        message = parsed_json["message"]
        print(status)
        if status == 201:
            print("Passed:  Favorite lists displayed successfully.")
        else:
            print("Failed:  Favorite lists not displayed successfully", message)





