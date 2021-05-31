from flask.wrappers import Response
from tests.base_test import BaseTest, db
from website.models import User
from flask_login import current_user

class TestLoginResponse(BaseTest):
    def test_login_loading_page(self):
        # test client and app context
        with self.app:
            response = self.app.get('/sign-up', content_type='html/text')
            self.assertEqual(response.status_code, 200)

class TestSignUp(BaseTest):

    # test signing up user successfully
    def test_sign_up_post_success(self):
        with self.app:
            # create a post req with valid data
            response = self.app.post('/sign-up',
                                    data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234', password2='pass1234'),
                                    follow_redirects=True)
            # assert that new user is created in db
            user = db.session.query(User).filter_by(email='email@gmail.com').first()
            self.assertTrue(user)
            # assert that flash message is shown
            self.assertIn(b'Account created', response.data)
            # assert that user is logged in
            self.assertEqual(current_user.get_id(), '1')
            # assert that page is redirected
            self.assertIn(b'Notes', response.data)

    def test_sign_up_post_wrong_email(self):
        with self.app:
            # create a post req with invalid email
            response = self.app.post('/sign-up',
                                    data=dict(email='lw', firstName='Namey', password1='pass1234', password2='pass1234'),
                                    follow_redirects=True)

            user = db.session.query(User).filter_by(email="me").first()

            self.assertFalse(user)

            self.assertIn(b'Email must be greater than 3 characters', response.data)

            self.assertIsNone(current_user.get_id())

            self.assertEqual(response.status_code, 200)

    def test_sign_up_post_1char_name(self):
        with self.app:
            # create a post req with invalid name
            response = self.app.post('/sign-up',
                                     data=dict(email='lwando@mail.com', firstName='N', password1='pass1234',
                                               password2='pass1234'),
                                     follow_redirects=True)

            user = db.session.query(User).filter_by(firstName='N').first()

            self.assertFalse(user)

            self.assertIn(b'', response.data)

            self.assertIsNone(current_user.get_id())

            self.assertEqual(response.status_code, 200)


    def test_password_dont_match(self):
        with self.app:
            response = self.app.post('/sign-up',
                                     data=dict(email="lwando@gmail.com", firstName="lwando", password1="123456", password2="1234"), follow_redirects=True)
            self.assertIn(b'', response.data)

