import unittest
import rsaidnumber


def verify():
    id_number = rsaidnumber.parse('0210160451089')
    return id_number.valid


def is_string():
    val = "khanya"
    return val.isdigit()


def is_digit():
    num = "67464"
    return num.isdigit()


class dataValidation(unittest.TestCase):
    def setUp(self):
        a = rsaidnumber.parse('0210160451089')


    def test_valid(self):
        self.assertEqual(verify(), True)


    def test_id(self):
        self.assertTrue(rsaidnumber.RSA_ID_LENGTH, 13)


    def test_string(self):
        self.assertFalse(is_string(), False)


    def test_integer(self):
        self.assertTrue(is_digit(), True)


if __name__ == '__main__':
    unittest.main()
