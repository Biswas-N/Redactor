import pytest

import project1


def test_sample_func():
    got = project1.sample_func()
    want = 22

    assert got == want
