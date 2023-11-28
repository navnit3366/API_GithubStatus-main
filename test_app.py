import unittest
import app


# pip install pytest
# pip install pytest-sugar


class TestStatus(unittest.TestCase):

    def test_get_one_json_status_by_id(self):
        with app.my_flask.test_client() as test:
            response = test.get('/24896kjk51045')
            json_data = response.get_json()
            self.assertEqual(response.status_code, 200)




