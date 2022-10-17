import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_contact_support(self):
        api_url = "https://some-URL/api/contact/support"
        email_id = ["card dev@sep27.com", "expire@test.com", "testmon@dom.cn", " ", "carddev@sep27.com"]
        subject = ["1QA", "", "58894556", "DSHFJHFJHFKS", "TESTING BY QA"]
        message_body = [ "ddggQA", "Qa768979", "", "%%&&", " Testing By QA"]
        for i, j, k in zip(email_id, subject, message_body):

            body = {

                "email": i,
                "subject": j,
                "message": k
            }
            print("email id, subject, message is:", i, j, k)
            r = requests.post(api_url, data=body)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            status = r.status_code
            message = parsed_json["message"]
            print(status)
            if status == 201:
                print("Passed: Message sent successfully.")
            else:
                print("Failed: Message not sent successfully.", message)
