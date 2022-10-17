import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_order_plan(self, auth_token_data):
        api_url = "https://some-URL/api/orders"
        access_token = auth_token_data
        print(access_token)
        assert access_token, "auth_token parameter should not be empty."
        for i in access_token:
            headers = {

                "authorization": i

            }
            body = {

                "payment_method_id": 8,
                "plan_id": 15,
                "amount": 10,
                "additional_devices": 2,
                "client_code": "pc"
            }
            print("\nauth token is:", i)
            r = requests.post(api_url, headers=headers, data=body)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            message = parsed_json["message"]
            print(status)
            if status == 201:
                print("Passed:  Order added successfully.")
            else:
                print("Failed:  Order not added successfully", message)

        x = "carddev@sep27.com"
        y = "123456"
        user_id, auth_token, password_encrypted = test_for_auth_token.Test.test_for_auth_token(self, x, y)
        assert auth_token, "auth_token parameter should not be empty."

        header = {

            "authorization": auth_token

        }
        body = {

            "payment_method_id": 13,
            "plan_id": 15,
            "amount": 10,
            "additional_devices": 2,
            "client_code": "pc"
        }
        r = requests.post(api_url, headers=header, data=body)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        status = r.status_code
        message = parsed_json["message"]
        print(status)
        if status == 201:
            print("Passed:  Order added successfully.")
        else:
            print("Failed:  Order not added successfully", message)





