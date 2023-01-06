import otpfunc
import unittest

class TestStringMethods(unittest.TestCase):

    def testcase1(self):
        Email = otpfunc.validate_email('ruddhibhagat2402@gmail.com')
        self.assertEqual(True,Email)

    def testcase2(self):
        size = 4
        Email = otpfunc. generate_otp()
        self.assertEqual(len(Email), size)

    def testcase3(self):
        Email = otpfunc.send_mail(otpfunc. generate_otp())
        self.assertEqual(True,Email)


if __name__ == '__main__':
    unittest.main()

