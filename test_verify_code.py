import json
import pytest
import requests


@pytest.mark.usefixtures("verify_code_data")
class Test:

    def test_verify_code(self, verify_code_data):

        api_url = "https://some-URL/api/verify/code"
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
                code = input("please enter the code received in email:")
                body = {
                    "email": i,
                    "verification_code": code
                }

                r = requests.post(api_url, data=body)
                parsed_json = (json.loads(r.content))
                print(json.dumps(parsed_json, indent=4, sort_keys=True))
                status = r.status_code
                print(status)
                if status == 201:
                    print("Passed: successfully verified the code, valid code")
                else:
                    print("Failed: unsuccessfully verified code or invalid code")
