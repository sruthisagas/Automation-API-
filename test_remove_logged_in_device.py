import json
import pytest
import requests


@pytest.mark.usefixtures("login_data")
class Test:

    def test_remove_logged_in_device(self, login_data):
        api_url = "https://some-URL/api/remove/loggedin/device"
        login_api_url = "https://some-URL/api/login"
        username = login_data[0]
        password = login_data[1]
        for i, j in zip(username, password):
            body = {
                "username": i,
                "password": j,
                "device_code": "api_device2",
                "device_name": "device_name window",
                "device_type": "windows",
                "lang": "EN",
                "version": "version"
            }
            print("\n", i, j)
            r = requests.post(login_api_url, data=body)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            message = parsed_json["message"]
            print(status)
            if status == 201 or message == "Please logout from other devices":
                access_token = parsed_json["accessToken"]
                user_devices_array = parsed_json["userDevicesArr"]
                length_devices_arr = len(user_devices_array)
                print("device array length:", length_devices_arr)
                print("device array", user_devices_array)
                if length_devices_arr > 0:
                    remove_device_id = user_devices_array[0]['id']
                    print(remove_device_id)

                    if user_devices_array:
                        remove_device_id = user_devices_array[0]['id']
                        headers = {

                            "authorization": access_token

                        }

                        body = {
                            "id": remove_device_id
                        }

                        r = requests.post(api_url, headers=headers, data=body)
                        print(r.status_code)
                        print(r.content)
                        print(length_devices_arr)
                        if r.status_code == 201:
                            print("Passed: Device Removed successfully.")
                        else:
                            print("Failed: Device Not Removed")
                else:
                    print("Current device cannot be removed")

            else:
                print("invalid account")





