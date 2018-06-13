import requests

from .auth import Auth


class Session(object):
    """
    Session handler for Marketo API

    Creates a new access_token and tracks its lifespan,
    refreshing if it runs out
    """

    def __init__(self, identity_url: str, client_id: str, client_secret: str):
        self.identity_url = identity_url
        self.client_id = client_id
        self.client_secret = client_secret

    def refresh_auth_token(self):
        """
        GETs a fresh auth token from the Marketo Identity auth endpoint

        Called when the session is initialized,
        and if the token reaches the end of its lifespan
        :return: None
        """
        pass
