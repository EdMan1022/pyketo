from . import BaseTestClass

from pyketo.auth import Auth


class TestAuth(BaseTestClass):

    target_path = 'pyketo.auth'

    def setUp(self):
        self.access_token = 'test'
        self.token_type = 'test'
        self.expires_in = 40
        self.scope = 'test'

    def test_init(self):
        auth = Auth(self.access_token, self.token_type, self.expires_in,
                    self.scope)

    def test_too_short_expires_in(self):
        with self.assertRaises(ValueError):
            Auth(self.access_token, self.token_type, 10, self.scope)


class TestSession(BaseTestClass):
    target_path = 'pyketo.session'

    def setUp(self):
        self.requests_patch = self.create_patch('requests')

        self.test_identity_url = 'test'
        self.test_client_id = 'test'
        self.test_client_secret = 'test'

        self.session = Session(
            self.test_identity_url,
            self.test_client_id,
            self.test_client_secret
        )

    def test_init(self):
        self.assertIsInstance(self.session, Session)

    def test_refresh_auth_token(self):
        old_token = self.session.auth.token
        old_token_created = self.session.auth.created_time
        self.session.refresh_auth_token()
        new_token = self.session.auth.token

        self.assertNotEqual(old_token, new_token)
