import sys
import unittest

from backports.httpmethod import HTTPMethod


class TestHTTPMethod(unittest.TestCase):
    def test_equals_string(self):
        self.assertEqual(HTTPMethod.GET, "GET")

    def test_value(self):
        self.assertEqual(HTTPMethod.GET.value, "GET")

    def test_description(self):
        self.assertEqual(HTTPMethod.GET.description, "Retrieve the target.")

    def test_available_methods(self):
        self.assertListEqual(
            list(HTTPMethod),
            [
                HTTPMethod.CONNECT,
                HTTPMethod.DELETE,
                HTTPMethod.GET,
                HTTPMethod.HEAD,
                HTTPMethod.OPTIONS,
                HTTPMethod.PATCH,
                HTTPMethod.POST,
                HTTPMethod.PUT,
                HTTPMethod.TRACE,
            ],
        )

    @unittest.skipIf(sys.version_info < (3, 11), "requires Python 3.11+")
    def test_equality(self):
        from http import HTTPMethod as PyHTTPMethod  # noqa: PLC0415

        self.assertEqual(HTTPMethod.__members__, PyHTTPMethod.__members__)
