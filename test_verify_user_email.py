import json
import pytest
import requests


@pytest.mark.usefixtures("verify_code_data")
class Test:

    def test_verify_user_email(self, verify_code_data):
        api_url = "https://some-URL/api/verify/email/code"
        username = verify_code_data
        for i in username:

            body = {
                "email": i
            }
            print(i)
            send_code_api_url = "https://some-URL/api/send/confirm/email/code"
            r = requests.post(send_code_api_url, data=body)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            if r.status_code == 201:
                code = input('please enter the verification code:')
                body = {
                    "email": i,
                    "verification_code": code,
                    "device_code": "device_code_xyz",
                    "device_name": "device_name window",
                    "device_type": "windows",
                    "lang": "EN",
                    "version": "version"
                }
                r = requests.post(api_url, data=body)
                parsed_json = (json.loads(r.content))
                print(json.dumps(parsed_json, indent=4, sort_keys=True))
                status = r.status_code
                print(status)
                if status == 201:
                    print("Email is verified Successfully with code.\n")
                else:
                    print("Failed: Email id not verified Successfully.\n")



