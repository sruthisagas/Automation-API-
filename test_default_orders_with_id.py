import json
import pytest
import requests
import test_for_auth_token


@pytest.mark.usefixtures("auth_token_data")
class Test:

    def test_default_orders_with_id(self, auth_token_data):

        """These api only send post or get request and see if proper error message is coming because payment gateway
          use these api and we can't send custom data to these default apis"""
        '''there will be no successful response only error response'''

        order_id_list = ["2946", "2895", "fdf", " "]
        for i in order_id_list:
            api_url = 'https://some-URL/api/orders/{}'.format(i)
            r = requests.get(api_url)
            print("order id id:", i)
            print(r.status_code)
            parsed_json = (json.loads(r.content))
            print(json.dumps(parsed_json, indent=4, sort_keys=True))
            if r.status_code != 201:
                print("Passed:  Error Message displayed as expected.")
            else:
                print("Failed:  Error Message not displayed as expected.")
