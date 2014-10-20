#!/usr/bin/env python2

import sys
import unittest
from tests.RequireMenuTestCase import AuthTestCase
from tests.ReloadPageTestCase import ReloadPageTestCase


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ReloadPageTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
