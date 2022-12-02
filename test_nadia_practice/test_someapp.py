import pytest

from someapp import join_str

def test_join_string_use_case():
    assert join_str([1, 2, 3],', ') == '1, 2, 3'

def test_join_string_single_case():
    assert join_str([1], ', ') == '1'

def test_join_string_delimiter():
    assert join_str([1, 2, 3], '') == '123'


