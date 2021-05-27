from tests.base_test import BaseTest

class TestLoginResponse(BaseTest):
    def test_login_loading_page(self):
        # test client and app context
        with self.app:
            response = self.app.get('/sign-up', content_type='html/text')
            self.assertEqual(response.status_code, 200)