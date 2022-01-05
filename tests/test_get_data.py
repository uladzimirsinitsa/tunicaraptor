
import unittest

from app import app

from werkzeug.exceptions import BadRequestKeyError


value = 'https://boxrec.com/en/proboxer/348759'


class TestGetData(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()
        with self.app as client:
            self.response = client.get('/v1/urls?key=https://boxrec.com/en/proboxer/348759').get_json()

    def test_get_data_1(self):
        self.assertEqual(self.response['url'], value, msg="Value 'url' invalid.")

    def test_get_data_2(self):
        self.assertEqual(self.response['key'], f'{value}', msg="Value 'key' invalid.")

    def test_get_data_3(self):
        self.assertIn(self.response['status_url'], ['processed', 'need_to_check'], msg="Value 'status_url' invalid.")

    def test_get_data_4(self):
        self.assertEqual(self.response['url'], self.response['key'], msg="Value 'url' and Value 'key' not equal.")

    def test_get_data_5(self):
        self.assertRaises(BadRequestKeyError)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
