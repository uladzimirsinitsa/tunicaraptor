
import unittest

from app import app


class TestDeleteData(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()

