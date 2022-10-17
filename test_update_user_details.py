import json
import unittest
import pytest
import requests

import test_for_auth_token
import test_user_login_password


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_update_user_details(self, auth_token_data):

        access_token = auth_token_data
        api_url = "https://some-URL/api/me/update"
        up_key = "preferred_language"
        up_val = "cn"
        for i in access_token:

            headers = {

                "authorization": i

            }
            body = {
                "update_key": up_key,
                "update_val": up_val,
                "current_password": "encrypted_pass(user current password)"
            }
            print(i)
            try:
                r = requests.post(api_url, headers=headers, data=body)
                print(r.status_code)
                if r.status_code == 201:
                    print("Passed: Details updated successfully.")
                else:
                    print("Failed: Details not updated successfully.")
            except Exception as inst:
                print(inst)

        user_name_data = "password20@gmail.com"
        user_password_data = "SRUTHI"
        user_id, auth_token, password_encrypted = test_for_auth_token.Test.test_for_auth_token(self, user_name_data,

                                                                                               user_password_data)

        update_headers = {

            "authorization": auth_token

        }
        update_body = {
            "update_key": up_key,
            "update_val": up_val,
            "current_password": password_encrypted
        }
        r = requests.post(api_url, headers=update_headers, data=update_body)
        print(r.status_code)
        if r.status_code == 201:
            print("Passed: Details updated successfully.")
        else:
            print("Failed: Details not updated successfully.")
        test_for_auth_token.Test.test_for_auth_token(self, user_name_data, user_password_data)



