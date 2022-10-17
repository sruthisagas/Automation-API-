import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_add_favorite(self):
        api_url = "https://some-URL/api/favorite"
        email_ids = [162, 164, 167, " ", "shffhs", 32434]
        for i in email_ids:

            body = {
                "device_code": "8A183C82-ABFB-4C53-A450-E34FA25C707C",
                "device_name": "Glaxy J3",
                "device_type": "android",
                "lang": "EN",
                "email": i,
                "password": "123456"
            }
            print("server node id is:", j)
            r = requests.post(api_url, data=body)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            message = parsed_json["message"]
            print(status)
            if status == 201:
                print("Passed:  Favorite added successfully.")
            else:
                print("Failed:  Favorite added not successfully", message)





