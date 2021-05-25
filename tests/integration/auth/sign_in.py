from urllib import request

from flask.wrappers import Response
from tests.base_test import BaseTest, db
from website.models import User
from flask_login import current_user


class TestSignIn(BaseTest):

    # test signing up user successfully
    def test_sign_in_post_success(self):
        with self.app:
            response = self.app.post('/sign-up',
                                        data={'email': 'lwando@meje.com', 'password': '12345'}, follow_redirects = (True))


            self.assertTrue(current_user.email == 'lwando@meje.com')
            self.assertTrue(current_user.password == '12345')



