import unittest

from learning.basic.identity import identity

class IdentityTest(unittest.TestCase):
    def test_identity_none(self):
        self.assertEqual(None, identity(None))

    def test_identity_number_0(self):
        self.assertEqual(0, identity(0))

    def test_identity_number_456(self):
        self.assertEqual(456, identity(456))

    def test_identity_string(self):
        self.assertEqual("example string", identity("example string"))

if __name__ == '__main__':
    unittest.main()
