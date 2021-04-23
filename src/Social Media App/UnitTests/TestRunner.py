# Combining Test Suites - unittest

#  ----------------- Unit test framework
import unittest, sys
sys.path.insert(0, './')

#  ----------------  Individual test suites - manual load
# UnitTests
'''from UnitTests.General.test_AddFollowers import TestAddFollowers
from UnitTests.General.test_Authentication import TestAuthentication
from UnitTests.General.test_DeleteFollowers import TestDeleteFollowers
from UnitTests.General.test_firebase_creds import TestFirebaseCreds
from UnitTests.General.test_QueryFollowers import TestQueryFollowers
from UnitTests.General.test_QueryProfile import TestQueryProfile

#NFR/FR Tests
from UnitTests.Function_NonFunc_UnitTests.test_FR_ST_1 import FR_ST_1
from UnitTests.Function_NonFunc_UnitTests.test_FR_ST_2 import FR_ST_2
from UnitTests.Function_NonFunc_UnitTests.test_FR_ST_4 import FR_ST_4
from UnitTests.Function_NonFunc_UnitTests.test_FR_ST_5 import FR_ST_5
from UnitTests.Function_NonFunc_UnitTests.test_FR_ST_7 import FR_ST_7
from UnitTests.Function_NonFunc_UnitTests.test_FR_ST_11 import FR_ST_11
from UnitTests.Function_NonFunc_UnitTests.test_NFR_PR_8 import NFR_PR_8
from UnitTests.Function_NonFunc_UnitTests.test_NFR_PR_10 import NFR_PR_10
from UnitTests.Function_NonFunc_UnitTests.test_NFR_SR_31 import NFR_SR_31
from UnitTests.Function_NonFunc_UnitTests.test_NFR_UH_6 import NFR_UH_6'''

# -----------------  Load all the test cases
'''suiteList = []
# Append General UnitTests
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(TestAddFollowers))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(TestAuthentication))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase( TestDeleteFollowers))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(TestFirebaseCreds))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(TestQueryFollowers))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(TestQueryProfile))
# Append FR/NFR Tests
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(FR_ST_1))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(FR_ST_2))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(FR_ST_4))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(FR_ST_7))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(FR_ST_11))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(NFR_PR_8))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(NFR_PR_10))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(NFR_SR_31))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(NFR_UH_6))

# ----------------   Join them together ane run them
comboSuite = unittest.TestSuite(suiteList)
unittest.TextTestRunner(verbosity=2).run(comboSuite)'''


# ALTERNATIVELY, discover all the tests in current directory dynamically(with name starting test_) and execute them!
loader = unittest.TestLoader()
tests = loader.discover('.')
testRunner = unittest.runner.TextTestRunner(verbosity=2)
testRunner.run(tests)