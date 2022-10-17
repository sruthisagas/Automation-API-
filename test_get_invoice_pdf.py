import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_get_invoice_pdf(self):

        api_url = 'https://some-URL/api/pdf'
        r = requests.get(api_url)
        print(r.status_code)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        if r.status_code == 201:
            print("Passed:  Record list displayed as expected.")
        else:
            print("Failed:  Record list not displayed as expected.")
