#!/usr/bin/env python2

import sys
import unittest
from tests.AgeRestrictionTestCase import AgeRestrictionInterfaceTestCase
from tests.ReqireMenuTestCase import ReloadPageTestCase
from tests.InterestTestCase import InterestInterfaceTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        #unittest.makeSuite(ReloadPageTestCase))
        unittest.makeSuite(AgeRestrictionInterfaceTestCase)))
    #    unittest.makeSuite(InterestInterfaceTest)),
    #))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
