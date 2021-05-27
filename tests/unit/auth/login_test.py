from website.models import User
from flask_login import current_user
from tests.base_test import BaseTest, db

class TestLoginResponse(BaseTest):
    def test_login_loading_page(self):
        # test client and app context
        with self.app:
            response = self.app.get('/log-in', content_type='html/text')
            self.assertEqual(response.status_code, 200)