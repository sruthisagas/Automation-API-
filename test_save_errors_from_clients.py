import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_save_errors_from_clients(self):

        api_url = 'https://some-URL/api/save/errors/vpn/connection'
        body = {
                "node_id": 6,
                "error_detail": "connect=succss",
                "device_detail": "{type:ios,name:iPad,extra:xyz detail}",
                "client_id": 2,
                "ip": "5.30.203.100"
            }
        r = requests.post(api_url, data=body)
        print(r.status_code)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        if r.status_code == 201:
            print("Passed:  Saved errors as expected.")
        else:
            print("Failed:  Errors not saved as expected.")
