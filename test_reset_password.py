import json
import os
import unittest

import pytest
import requests

import test_send_confirmation_code_to_email
import test_user_login_password
import subprocess


@pytest.mark.usefixtures("reset_password_data")
class Test:

    def test_reset_password(self, reset_password_data):

        list_of_usernames = reset_password_data
        print(list_of_usernames)
        for j in list_of_usernames:
            print("\n", j)
            body = {
                "email": j
            }

            send_code_api_url = "https://some-URL/api/send/confirm/email/code"
            r = requests.post(send_code_api_url, data=body)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            if r.status_code == 201:
                code = input("please enter verification code received in email:")
                new_password = input("please enter new password:")
                api_url = "https://some-URL/api/reset/password"
                body = {
                    "email": j,
                    "verification_code": code,
                    "new_password": new_password
                }
                print(j, code, new_password)
                r = requests.post(api_url, data=body)
                parsed_json = (json.loads(r.content))
                print(json.dumps(parsed_json, indent=4, sort_keys=True))
                status = r.status_code
                print(status)
                if status == 201:
                    print("Passed: Password reset completed successfully")
                else:
                    print("Failed: Unable to reset password.")

            else:
                print("Error in email id")





