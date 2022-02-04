import json
import math

import pytest
import requests
from hamcrest import *

headers = {
    'User-Agent': 'Python Learning Requests',
    'content-type': 'application/json'
}


@pytest.mark.fixtures("rounding_index")
class TestCalc:

    @pytest.mark.parametrize("x", [1, 4, 9, 16, 25])
    @pytest.mark.parametrize("y", [-1, -4, 9, 0, 25])
    def test_sum(self, x, y):
        request_data = {"expr": str(x) + " + " + str(y)}
        result = requests.post("http://api.mathjs.org/v4/", data=json.dumps(request_data), headers=headers).json()
        assert_that(result["result"], equal_to(str(x + y)), 'Sum is invalid')

    @pytest.mark.parametrize("x", [1, 4, 9, 16, 25])
    @pytest.mark.parametrize("y", [-1, -4, 9, 0, 25])
    def test_subtract(self, x, y):
        request_data = {"expr": str(x) + " - " + str(y)}
        result = requests.post("http://api.mathjs.org/v4/", data=json.dumps(request_data), headers=headers).json()
        assert_that(result["result"], equal_to(str(x - y)), 'Subtract is invalid')

    @pytest.mark.parametrize("x", [1, 4, 9, 16, 25])
    @pytest.mark.parametrize("y", [-1, -4, 9, 0, 25])
    def test_multiply(self, x, y):
        request_data = {"expr": str(x) + " * " + str(y)}
        result = requests.post("http://api.mathjs.org/v4/", data=json.dumps(request_data), headers=headers).json()
        assert_that(result["result"], equal_to(str(x * y)), 'Multiply is invalid')

    @pytest.mark.parametrize("x", [1, 4, 9, 16, 25])
    @pytest.mark.parametrize("y", [-1, -4, 9, 4, 25])
    def test_divide(self, x, y):
        request_data = {"expr": str(x) + " / " + str(y)}
        result = requests.post("http://api.mathjs.org/v4/", data=json.dumps(request_data), headers=headers).json()
        assert_that(float(result["result"]), equal_to(float(str(x / y))), 'Divide is invalid')

    @pytest.mark.parametrize("x", [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
    def test_square_root(self, x):
        result = requests.get('http://api.mathjs.org/v4/?expr=sqrt(' + str(x) + ')', headers=headers).text
        assert_that(float(str(result) + ".0"), equal_to(math.sqrt(x)), 'Square root is invalid')

