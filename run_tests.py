#!/usr/bin/env python2

import sys
import unittest
from tests.AgeRestrictionTestCase import AgeRestrictionTestCase
from tests.ReqireMenuTestCase import RequireMenuTestCase
from tests.InterestTestCase import InterestTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(RequireMenuTestCase),
        unittest.makeSuite(AgeRestrictionTestCase),
        unittest.makeSuite(InterestTest))
    )
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
