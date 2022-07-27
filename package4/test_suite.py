import unittest
from package1.Login import LoginTest
from package1.Login1 import Login
from package2.Booking import Bookingtest
from package2.Register import Registertest
tc1=unittest.TestLoader().loadTestsFromTestCase(Login)
tc2=unittest.TestLoader().loadTestsFromTestCase(Registertest)
tc3=unittest.TestLoader().loadTestsFromTestCase(Bookingtest)
masterTestSuite=unittest.TestSuite([tc1,tc2,tc3])
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)
