import unittest
import rsaidnumber


def verify():
    id = rsaidnumber.parse('0210160451089')
    return id.valid


class ValidID(unittest.TestCase):
    def setUp(self):
        a = rsaidnumber.parse('0210160451089')


    def test_valid(self):
        self.assertEqual(verify(), True)


    def test_id(self):
        self.assertTrue(rsaidnumber.RSA_ID_LENGTH, 13)


if __name__ == '__main__':
    unittest.main()
