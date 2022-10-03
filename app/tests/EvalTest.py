import unittest

from unittest2 import TestCase
import app.client as client
from parameterized import parameterized


class EvalTest(TestCase):
    @parameterized.expand(
        [
            (10, 10, "+", 20),
            (1, 2, "/", 0),
            (2, 10, "**", 1024),
            (10001, 1, "-", 10000),
            (237, 3, "%", 0),
        ]
    )
    def test_basic_operations(self, rhs, lhs, op, res):
        result = client.run(rhs, lhs, op)
        self.assertTrue(result.operation == op and result.result == res)

    @parameterized.expand([(101, 101, "***", 1), (101, 101, "//", 1)])
    def test_unsupported_operations(self, rhs, lhs, op, error):
        result = client.run(rhs, lhs, op)
        self.assertTrue(result.result == 0 and result.error == error)


if __name__ == "__main__":
    unittest.main()
