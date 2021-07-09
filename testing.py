import unittest
import rsaidnumber


def verify():
    id = rsaidnumber.parse('0210160451089')
    return id.valid


def is_string():
        val = "khanya"
        return val.isdigit()


def is_digit():
        num = "67464"
        return num.isdigit()


class Data_Validation(unittest.TestCase):
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



# def test_str():
#         val = "khanya"
#         return val.isdigit()
#
#
# class validation(unittest.TestCase):
#
#     def is_string(self):
#         val = "khanya"
#         self.assertFalse(test_str(), False)
#
#
#     def is_integer(self):
#         num = "73920"
#         self.assertTrue(num, True)


if __name__ == '__main__':
    unittest.main()
