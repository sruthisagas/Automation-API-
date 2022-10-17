import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_redeem_gift(self, auth_token_data):
        api_url = "https://some-URL/api/redeem/gift"
        access_token = auth_token_data
        print(access_token)
        assert access_token, "auth_token parameter should not be empty."
        for i in access_token:
            headers = {

                "authorization": i

            }

            body = {
                "gift_code": "AHGSDYUJFDG",
                "client_code": "web",
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

        gift_code = ["fDbdacjqkcfnarga", " ", "babbabanaanadhdb", "fpdceaahaxbbcCch", "0' AND 1=2--", "' OR 1=1--"]
        for j in gift_code:

            header = {

                "authorization": auth_token

            }
            body = {
                "gift_code": j,
                "client_code": "web",
                "lang": "EN"
            }

            print("\n Gift Code is:", j)
            r = requests.post(api_url, data=body, headers=header)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            message = parsed_json["message"]
            print(status)
            if status == 201:
                print("Passed: Code redeemed successfully.")
            else:
                print("Failed: Code not redeemed successfully.", message)





