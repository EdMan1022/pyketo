import requests

from .auth import Auth


class Session(object):
    """
    Session handler for Marketo API

    Creates a new access_token and tracks its lifespan,
    refreshing if it runs out
    """

    refresh_token_url = "oauth/token"
    header_key = 'headers'
    access_token_key = 'Authorization'

    def __init__(self, base_url: str, identity_url: str, client_id: str,
                 client_secret: str, auto_base: bool=True):

        self._auth = None

        self.base_url = base_url
        self.identity_url = identity_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.auto_base = auto_base

    def refresh_auth_token(self):
        """
        GETs a fresh auth token from the Marketo Identity auth endpoint

        Called when the session is initialized,
        and if the token reaches the end of its lifespan
        :return: None
        """

        # Set up the parameters needed to refresh the API token
        auth_token_params = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }

        # Use the requests package to make the refresh request
        auth_response = requests.get(
            url="{}/{}".format(self.identity_url, self.refresh_token_url),
            params=auth_token_params
        )

        # Initialize a new Auth instance using the response
        self._auth = Auth(**auth_response.json())

    @property
    def auth(self):

        if not self._auth:
            self.refresh_auth_token()

        elif self._auth.expired():
            self.refresh_auth_token()

        return self._auth

    @property
    def auth_header(self):
        return "{} {}".format(self.auth.type, self.auth.access_token)

    def _http_request(self, *args, **kwargs):
        if kwargs.get(self.header_key):
            kwargs[self.header_key][self.access_token_key] = \
                self.auth_header
        else:
            kwargs[self.header_key] = \
                {self.access_token_key: self.auth_header}
        return args, kwargs

    def get(self, *args, **kwargs):
        args, kwargs = self._http_request(*args, **kwargs)
        return requests.get(*args, **kwargs)


