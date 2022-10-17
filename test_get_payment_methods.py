import json
import requests


class Test:

    def test_get_payment_methods(self):
        api_url = "https://some-URL/api/paymentmethods"
        r = requests.get(api_url)
        parsed_json = (json.loads(r.content))
        print(json.dumps(parsed_json, indent=4, sort_keys=True))
        status = r.status_code
        print(status)
        if status == 201:
            print("Passed: Available payment methods displayed successfully.")
        else:
            print("Failed: Available payment methods not displayed successfully.")





