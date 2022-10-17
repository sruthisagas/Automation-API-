import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_get_user_shortcut_links(self):
        api_url = "https://some-URL/api/test/all/email/templates"
        email_id = ["card dev@sep27.com", "expire@test..com", "testmon@", "carddev@sep27.com"]
        for i in email_id:

            body = {
                "lang": "EN",
                "email": i,
                "save_code": "0",
                "dummy_password": "1123adsf",
                "verification_code": "123456",
                "invite_code": "123456"
            }
            print("email id is :", i)
            r = requests.post(api_url, data=body)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            message = parsed_json["message"]
            print(status)
            if status == 201:
                print("Passed: user shortcut links displayed successfully.")
            else:
                print("Failed: user shortcut links not displayed successfully", message)

