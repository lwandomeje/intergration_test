from website.models import User
from flask_login import current_user
from tests.base_test import BaseTest, db

class Testing(BaseTest):
    def test_login_correct_email_firstname(self):
        with self.app:
            # create a post req with valid data
            response = self.app.post('/sign-up',
                                     data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234',
                                               password2='pass1234'),
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

            resp = self.app.post('/log-in', data=dict(email='email@gmail.com',
                                                      password='pass1234'), follow_redirects=True)
            self.assertIn(b'Logged in successfully', resp.data)



    def test_login_incorrect_email_firstname(self):
        with self.app:
            # create a post req with valid data
            response = self.app.post('/sign-up',
                                     data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234',
                                               password2='pass1234'),
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

            #log in with incorrect email
            resp = self.app.post('/log-in', data=dict(email='abcd@gmail.com',
                                                      password='pass12345'), follow_redirects=True)
            self.assertIn(b'Email does not exist', resp.data)

    def test_login_incorrect_password_firstname(self):
        with self.app:
            # create a post req with valid data
            response = self.app.post('/sign-up',
                                     data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234',
                                               password2='pass1234'),
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

            # log in with incorrect email and
            resp = self.app.post('/log-in', data=dict(email='email@gmail.com',
                                                      password='pass1234'), follow_redirects=True)
            self.assertIn(b'',resp.data)








