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