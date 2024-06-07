import unittest
from time_tracker.wsgi import application as wsgi_application
from time_tracker.asgi import application as asgi_application


class WSGITestCase(unittest.TestCase):
    def test_application_exists(self):
        self.assertIsNotNone(wsgi_application)


class ASGITestCase(unittest.TestCase):
    def test_application_exists(self):
        self.assertIsNotNone(asgi_application)


if __name__ == "__main__":
    unittest.main()
