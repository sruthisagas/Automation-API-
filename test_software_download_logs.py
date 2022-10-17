import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_software_download_logs(self):

        api_url = 'https://some-URL/api/software-download-logs'
        body = {
            "source_type": "1",
            "ip": "5.30.203.100",
            "action_id": "56465456456",
            "channel": "google",
            "client": "pc",
            "url": "https://swoshsvpn.com/download-vpn-for-android",
            "session": "user_id"
            }
        r = requests.post(api_url, data=body)
        print(r.status_code)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        if r.status_code == 201:
            print("Passed:  Software download logs displayed as expected.")
        else:
            print("Failed:  Software download logs not displayed as expected.")
