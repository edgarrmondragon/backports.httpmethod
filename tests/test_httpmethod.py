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
                HTTPMethod.QUERY,
                HTTPMethod.TRACE,
            ],
        )

    @unittest.skipIf(sys.version_info < (3, 11), "requires Python 3.11+")
    def test_equality(self):
        from http import HTTPMethod as PyHTTPMethod  # ruff:ignore[import-outside-top-level]

        expected = dict(HTTPMethod.__members__)

        # Specifically first shipped in 3.16.0a3
        if sys.version_info < (3, 16):
            del expected[HTTPMethod.QUERY]

        self.assertEqual(expected, dict(PyHTTPMethod.__members__))
