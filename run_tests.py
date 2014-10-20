#!/usr/bin/env python2

import sys
import unittest
from tests.AgeRestrictionInterfaceTestCase import AgeRestrictionInterfaceTestCase
from tests.ReloadPageTestCase import ReloadPageTestCase


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(#ReloadPageTestCase,
                           AgeRestrictionInterfaceTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
