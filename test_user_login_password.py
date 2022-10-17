import json
import pytest
import requests


@pytest.mark.usefixtures("login_data")
class Test:

    def test_user_login_password(self, login_data):

        api_url = "https://some-URL/api/login"
        username = login_data[0]
        password = login_data[1]
        successful_username = ""
        access_token = ""
        encrypted_password = ""
        for i, j in zip(username, password):
            body = {
                "username": i,
                "password": j,
                "device_code": "api_device",
                "device_name": "device_name window",
                "device_type": "windows",
                "lang": "EN",
                "version": "version"
            }
            print("\n", i, j)
            r = requests.post(api_url, data=body)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            print(status)
            if status == 201:
                access_token = parsed_json["accessToken"]
                successful_username = parsed_json["username"]
                encrypted_password = parsed_json["password"]
                print("Passed: User Logged in successfully.")
            else:
                print("Failed: User not Logged in.")

        if successful_username != "":
            return successful_username, access_token, encrypted_password

