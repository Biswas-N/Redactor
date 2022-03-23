from typing import Any
from project1 import models

def test_settings():
    # False Case
    temp_args: dict[str, Any] = {
        'input': ['*.csv', '*.txt'],
        'output': 'files/'
    }

    got = models.Settings.parse(temp_args)
    want = models.Settings(
        input=['*.pdf'],
        output='file/')

    assert got != want

    # True Case
    temp_args: dict[str, Any] = {
        'input': ['*.csv', '*.txt'],
        'output': 'files/'
    }

    got = models.Settings.parse(temp_args)
    want = models.Settings(
        input=['*.txt', '*.csv'],
        output='files/')

    assert got == want
