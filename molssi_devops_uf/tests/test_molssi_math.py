'''
Tests for the math module
'''

import pytest
import molssi_devops_uf as ms_uf

@pytest.mark.parametrize('lst, mean', [([1, 2, 3, 4, 5], 3), ([-2, -1, 0, 1, 2], 0)])

def test_many(lst, mean):
    assert ms_uf.my_mean(lst) == mean 

def test_molssi_math_mean():
    test_val = ms_uf.my_mean([1, 2, 3, 4, 5])
    assert test_val == 3.0

def test_molssi_types():
    with pytest.raises(TypeError):
        ms_uf.my_mean('Thestringtype')

