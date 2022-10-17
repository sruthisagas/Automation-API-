import json
import unittest
import pytest
import requests


@pytest.mark.usefixtures("send_code_data")
class Test:

    def test_send_confirmation_code_to_mail(self, send_code_data):

        successful_username = ""
        api_url = "https://some-URL/api/send/confirm/email/code"
        username = send_code_data
        print(username)
        for i in username:
            body = {
                "email": i
            }
            print("\n", i)
            r = requests.post(api_url, data=body)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            print(status)
            if status == 201:
                successful_username = i
                print("Passed: successfully sent confirmation code to email id :", successful_username)
            else:
                print("Failed: Unable to send confirmation code to email id")

        if successful_username != "":
            return successful_username

