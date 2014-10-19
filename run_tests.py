#!/usr/bin/env python2

import sys
import unittest
from tests.AuthTestCase import AuthTestCase


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
