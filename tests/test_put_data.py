
import unittest
from app import app


class TestPutData(unittest.TestCase):
    
    def setUp(self) -> None:
        self.app = app.test_client()
        with self.app as client:
            data = {'url': 'test_str', 'status_url': 'processed', 'number_CPU': 1}
            self.r = client.post('/v1/urls', json=data)


    def test_put_data_1(self):
        with self.app as client:
            response = client.get('/v1/urls?key=test_str').get_json()
        self.assertEqual(response['url'], 'test_str', msg="Value 'url' invalid.")


if __name__ == '__main__':
    unittest.main()