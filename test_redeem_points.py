import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtuers("auth_token_data")
class Test:

    def test_redeem_points(self, auth_token_data):
        api_url = "https://some-URL/api/redeem/points"
        access_token = auth_token_data
        print(access_token)
        assert access_token, "auth_token parameter should not be empty."
        for i in access_token:
            headers = {

                "authorization": i

            }

            point = 100
            body = {
                "points": point,
                "client_code": "web",
                "lang": "EN"
            }

            r = requests.post(api_url, data=body, headers=headers)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            message = parsed_json["message"]
            print(status)
            if status == 201:
                print("Passed: Point redeemed successfully.")
            else:
                print("Failed: Point not redeemed.", message)

        user_name_data = "carddev@sep27.com"
        user_password_data = "123456"
        user_id, auth_token, password_encrypted = test_for_auth_token.Test.test_for_auth_token(self, user_name_data,

                                                                                               user_password_data)
        assert auth_token, "auth_token parameter should not be empty."
        header = {

            "authorization": auth_token

        }
        point_redeem = ['sfsaf', '$@$%', 1000, 101, 99, ' ', 100]
        for j in point_redeem:
            body_redeem = {
                "points": j,
                "client_code": "web",
                "lang": "EN"
            }
            print("user try to redeem point is", j)
            r = requests.post(api_url, headers=header, data=body_redeem)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            if r.status_code == 201:
                print("Passed: Details updated successfully.")
            else:
                print("Failed: Details not updated successfully.")



