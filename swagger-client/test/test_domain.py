# coding: utf-8

"""
    Platform API

    The REST API for Platform.sh.

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.domain import Domain


class TestDomain(unittest.TestCase):
    """ Domain unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDomain(self):
        """
        Test Domain
        """
        model = swagger_client.models.domain.Domain()


if __name__ == '__main__':
    unittest.main()
