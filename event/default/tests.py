from django.test import TestCase

# Create your tests here.

class Views_test(TestCase):
    def test_index_view(self):
        self.assertEqual(self.client.get('/').status_code, 200)

    def test_login_view(self):
        self.assertEqual(self.client.get('/login/').status_code, 200)

    def test_contact_us_view(self):
        self.assertEqual(self.client.get('/contact_us/').status_code, 200)
    
    def test_insert_into_db_view(self):
        self.assertEqual(self.client.get('/insert_into_db/').status_code, 200)
        