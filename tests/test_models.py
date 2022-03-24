import pytest
from project1 import models

test_cases = [
    ({'input': ['*.csv', '*.txt'], 'output': 'files/', 'names': True},
        models.Settings(input=['*.txt', '*.csv'], output='files/', redacts={'names': True}),
        True),
    ({'input': ['*.pdf'], 'output': 'files/1', 'names': True},
        models.Settings(input=['*.txt', '*.csv'], output='files/', redacts={'names': True}),
        False),
    ({'input': ['*.csv', '*.txt'], 'output': 'dummy/', 'names': True},
        models.Settings(input=['*.txt', '*.csv'], output='files/', redacts={'names': True}),
        False),
    ({'input': ['*.csv', '*.txt'], 'output': 'files/', 'names': True},
        models.Settings(input=['*.txt', '*.csv'], output='files/', redacts={'names': False}),
        False),
    ({'input': ['*.csv', '*.txt'], 'output': 'files/', 'names': True},
        models.Settings(input=['*.txt', '*.csv'], output='files/', redacts={'names': False, 'dummy': True}),
        False),
]


@pytest.mark.parametrize("input,want,result", test_cases)
def test_settings_dunder_equal_func(input, want, result):
    got = models.Settings.parse(input)

    assert (got == want) is result


def test_settings_dunder_str_func():
    args_in = {'input': ['*.csv', '*.txt'], 'output': 'files/', 'names': True}
    args_out = {
        'input': [
            '*.csv',
            '*.txt'],
        'output': 'files/',
        'redacts': {
            'names': True}}

    got = models.Settings.parse(args_in)
    want = 'Settings (\n\tinput: {0}\n\toutput: {1}\n\tredacts: {2}\n)'.format(
        str(args_out['input']), args_out['output'], str(args_out['redacts']))

    assert str(got) == want
