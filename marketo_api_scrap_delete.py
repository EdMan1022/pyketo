import json
import os

from pyketo import Session
import requests


marketo_id = os.environ["MARKETO_CLIENT_ID"]
marketo_secret = os.environ["MARKETO_CLIENT_SECRET"]
marketo_user = os.environ["MARKETO_AUTHORIZED_USER"]
marketo_base_url = os.environ["MARKETO_BASE_URL"]
marketo_identity_url = "{}/identity".format(marketo_base_url)

session = Session(
    marketo_base_url, marketo_identity_url, marketo_id, marketo_secret
)

params = {
    "filterType": "id",
    "filterValues": "4201568"
}

data = {
    "input": [
        {"id": 4201641},
        {"id": 4201642},
        {"id": 4201643},
        {"id": 4201644},
        {"id": 4201645},
    ]
}


response = session.delete('leads.json', json=data)

response_data = response.json()

with open('responses/multi_id_delete_lead.json', 'w') as file_obj:
    json.dump(response_data, file_obj)

