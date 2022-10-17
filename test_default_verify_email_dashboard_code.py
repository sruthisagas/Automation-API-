import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_default_verify_email_dashboard_code(self):

        """These api only send post or get request and see if proper error message is coming because payment gateway
          use these api and we can't send custom data to these default apis"""
        '''there will be no successful response only error response'''

        api_url = 'https://some-URL/api/verify/email/dashboard/code'
        r = requests.post(api_url)
        print(r.status_code)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        if r.status_code != 201:
            print("Passed:  Error Message displayed as expected.")
        else:
            print("Failed:  Error Message not displayed as expected.")
