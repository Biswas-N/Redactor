import pytest
from project1 import models

test_cases = [
    ({'input': ['*.csv', '*.txt'],'output': 'files/'},
        models.Settings(input=['*.txt', '*.csv'],output='files/'),
        True),
    ({'input': ['*.pdf'],'output': 'files/'},
        models.Settings(input=['*.txt', '*.csv'],output='files/'),
        False),
    ({'input': ['*.csv', '*.txt'],'output': 'dummy/'},
        models.Settings(input=['*.txt', '*.csv'],output='files/'),
        False)
]

@pytest.mark.parametrize("input,want,result", test_cases)
def test_settings_dunder_equal_func(input, want, result):
    got = models.Settings.parse(input)

    assert (got == want) is result

def test_settings_dunder_str_func():
    temp_args = {'input': ['*.csv', '*.txt'],'output': 'files/'}
    got = models.Settings.parse(temp_args)
    want = 'Settings (\n\tinput: {0}\n\toutput: {1}\n)'.format(str(temp_args['input']), temp_args['output'])

    assert str(got) == want