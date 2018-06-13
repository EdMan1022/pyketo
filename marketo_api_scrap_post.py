import json
import os

from pyketo import Session
import requests

marketo_id = os.environ["MARKETO_CLIENT_ID"]
marketo_secret = os.environ["MARKETO_CLIENT_SECRET"]
marketo_user = os.environ["MARKETO_AUTHORIZED_USER"]
marketo_base_url = os.environ["MARKETO_BASE_URL"]
marketo_identity_url = "{}/identity".format(marketo_base_url)
test_user_domain = os.environ['TEST_USER_DOMAIN']

session = Session(
    marketo_base_url, marketo_identity_url, marketo_id, marketo_secret
)

test_data = {
    "action": "createOnly",
    "lookupField": "email",
    "input": [
        {"email": "test{}@{}".format(i, test_user_domain)}
        for i in range(5)
    ]
}

response = session.post('leads.json', json=test_data)
response_data = response.json()

with open('responses/new_test_lead.json', 'w') as file_obj:
    json.dump(response_data, file_obj)
