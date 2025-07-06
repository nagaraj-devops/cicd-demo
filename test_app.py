import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Hello World!")

if __name__ == '__main__':
    unittest.main()
# This code is a unit test for the Flask application defined in app.py.
# It uses the unittest framework to create a test case that checks if the root URL ("/") returns a 200 status code and the expected response "Hello World!".
# The test case is run when the script is executed directly, allowing for automated testing of the Flask application.
# The `setUp` method initializes the test client for the Flask app, which is used to simulate requests to the application during testing.
# The `test_hello` method sends a GET request to the