# -*- coding: utf-8 -*-

import pytest
from python_package_template.skeleton import fib

__author__ = "sirtyman"
__copyright__ = "sirtyman"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
