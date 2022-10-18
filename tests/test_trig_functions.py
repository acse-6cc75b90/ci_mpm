import pytest

from numpy import pi, isclose
from simple_functions import sin


class TestTrigFuncions(object):
    '''Class to test our trigonometric functions are working correctly'''

    @pytest.mark.parametrize('x, expected', [
        (0, 0),
        (.5 * pi, 1),
        (pi, 0),
        (1.5 * pi, -1),
    ])
    def test_my_add(self, x, expected):
        '''Test our add function'''
        isum = sin(x)
        assert isclose(isum, expected).all()
