import json
import pytest
import requests


@pytest.mark.usefixtures("login_code_data")
class Test:

    def test_user_login_with_code(self, login_code_data):
        api_url = "https://some-URL/api/login/with/code"
        username = login_code_data
        for i in username:
            print(i)
            body = {
                "username": i
            }
            print("\n", i)
            r = requests.post(api_url, data=body)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            print(status)
            if status == 201:
                print("Passed: Successfully send verification code to user email address. please check...")
                login_code = input('please enter verification code received:')
                assert login_code, "login code parameter should not be empty. "
                body = {
                    "username": i,
                    "login_code": login_code
                }
                r = requests.post(api_url, data=body)
                parsed_json = (json.loads(r.content))
                print(json.dumps(parsed_json, indent=4, sort_keys=True))
                status = r.status_code
                print(status)
                if status == 201:
                    print("Passed: Successfully logged into SwoshsVPN.")
                else:
                    print("Failed: unable to login with code")
            else:
                print("Failed: unable to send code for user login")




