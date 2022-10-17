import json
import pytest as pytest
import requests


@pytest.mark.usefixtures("registration_data")
class Test:

    def test_new_user_registration(self, registration_data):

        api_url = "https://some-URL/api/register"
        username = registration_data[0]
        password = registration_data[1]
        print(username, len(username))
        print(password, len(password))

        for i, j in zip(username, password):
            body = {
                "username": i,
                "password": j,
                "verification_required": 2,
                "channel_id": 8,
                "device_type": "android",
                "invite_code": "9i4j6v2r"
            }
            print("\n", i, j)
            r = requests.post(api_url, data=body)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            print(status)
            if status == 201:
                print("Passed: Registration Completed successfully.")
            else:
                print("Failed: registration not completed successfully")


