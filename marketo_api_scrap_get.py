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

emails = [
    "test{}@{}".format(i, test_user_domain)
    for i in range(5)
]


params = {
    "filterType": "email",
    "filterValues": ','.join(emails)
}

response = session.get('leads.json', params=params)
response_data = response.json()

with open('responses/email_get.json', 'w') as file_obj:
    json.dump(response_data, file_obj)
