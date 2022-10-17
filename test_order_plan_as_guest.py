import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_order_plan_as_guest(self):
        api_url = "https://some-URL/api/orders/as/guest"
        params = {

            "lang": "en"

        }
        email_id = ["card dev@sep27.com", "expire@test..com", "testmon@", "carddev@sep27.com", "john@example.com"]
        for i in email_id:

            body = {
                "email": i,
                "payment_method_id": 8,
                "plan_id": 15,
                "amount": 10,
                "additional_devices": 2,
                "client_code": "pc"
            }
            print("\nauth token is:", i)
            r = requests.post(api_url, params=params, data=body)
            print(r.status_code)
            if r.status_code == 201:
                print("Passed:  Order added successfully as guest.")
            else:
                print("Failed:  Order not added successfully as guest.")







