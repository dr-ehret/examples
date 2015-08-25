import numpy

from numpy import array
from numpy.testing import assert_array_equal


def test_slicing():
    from numpy import array
    x = array([[1, 2, 3], [4, 5, 6]])
    assert_array_equal(x[:, ::2], array([[1, 3], [4, 6]]))

print(test_slicing()) # => None
