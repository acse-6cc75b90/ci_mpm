import pytest
# from Lectures.Lecture06.ci_mpm.simple_functions.functions1 import factorial

from simple_functions import my_sum, factorial


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1),
        (0, 1),
    ])
    def test_factorial(self, number, expected):
        '''Test our factorial function'''
        result = factorial(number)
        assert result == expected
