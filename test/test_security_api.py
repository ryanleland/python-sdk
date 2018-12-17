# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import intrinio_sdk
from intrinio_sdk.api.security_api import SecurityApi  # noqa: E501
from intrinio_sdk.rest import ApiException


class TestSecurityApi(unittest.TestCase):
    """SecurityApi unit test stubs"""

    def setUp(self):
        self.api = intrinio_sdk.api.security_api.SecurityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_securities(self):
        """Test case for get_all_securities

        Get All Securiites  # noqa: E501
        """
        pass

    def test_get_security_by_id(self):
        """Test case for get_security_by_id

        Get a Security by ID  # noqa: E501
        """
        pass

    def test_get_security_data_point_number(self):
        """Test case for get_security_data_point_number

        Get Security Data Point (Number)  # noqa: E501
        """
        pass

    def test_get_security_data_point_text(self):
        """Test case for get_security_data_point_text

        Get Security Data Point (Text)  # noqa: E501
        """
        pass

    def test_get_security_historical_data(self):
        """Test case for get_security_historical_data

        Get Security Historical Data  # noqa: E501
        """
        pass

    def test_get_security_stock_price_adjustments(self):
        """Test case for get_security_stock_price_adjustments

        Get Stock Price Adjustments for Security  # noqa: E501
        """
        pass

    def test_get_security_stock_prices(self):
        """Test case for get_security_stock_prices

        Get Stock Prices for Security  # noqa: E501
        """
        pass

    def test_screen_securities(self):
        """Test case for screen_securities

        Screen Securities  # noqa: E501
        """
        pass

    def test_search_securities(self):
        """Test case for search_securities

        Search Securities  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
