import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_get_orders_by_id(self, auth_token_data):
        api_url = "https://some-URL/api/orders"
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
                print("Passed:  Order lists displayed successfully.")
            else:
                print("Failed:  Order lists not displayed successfully", message)

        x = "carddev@sep27.com"
        y = "123456"
        user_id, auth_token, password_encrypted = test_for_auth_token.Test.test_for_auth_token(self, x, y)
        assert auth_token, "auth_token parameter should not be empty."

        header = {

            "authorization": auth_token

        }
        order_id_list = ["2946", "2895", "fdf", " "]
        for i in order_id_list:
            api_url = 'https://apidev.swoshstest.com/api/orders/{}'.format(i)
            r = requests.get(api_url, headers=header)
            print("order id id:", i)
            print(r.status_code)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            if r.status_code == 201:
                print("Passed:  Order lists displayed successfully.")
            else:
                print("Failed:  Order lists not displayed successfully")






