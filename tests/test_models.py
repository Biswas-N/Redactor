import pytest
from project1 import models

test_cases = [
    ({'input': ['*.csv', '*.txt'], 'output': 'files/', 'names': True, 'concept': ['kids', 'war'], 'stats': 'stdout'},
        models.Settings(
        input=[
            '*.txt',
            '*.csv'],
        output='files/',
        redacts={
            'names': True},
        concepts=['kids', 'war'],
        stats='stdout'),
        True),
    ({'input': ['*.csv', '*.txt'], 'output': 'dummy/', 'names': True, 'concept': ['kids'], 'stats': 'stdout'},
        models.Settings(
        input=[
            '*.txt'],
        output='files/',
        redacts={
            'names': True},
        concepts=['kids', 'war'],
        stats='stdout'),
        False),
    ({'input': ['*.csv', '*.txt'], 'output': 'files/', 'names': True, 'concept': ['kids'], 'stats': 'stdout'},
        models.Settings(
        input=[
            '*.txt',
            '*.csv'],
        output='dummy/',
        redacts={
            'names': True},
        concepts=['kids', 'war'],
        stats='stdout'),
        False),
    ({'input': ['*.csv', '*.txt'], 'output': 'files/', 'names': True, 'concept': ['kids'], 'stats': 'stdout'},
        models.Settings(
        input=[
            '*.txt',
            '*.csv'],
        output='files/',
        redacts={
            'names': True,
            'genders': False},
        concepts=['kids', 'war'],
        stats='stdout'),
        False),
    ({'input': ['*.csv', '*.txt'], 'output': 'files/', 'names': True, 'genders': True, 'concept': ['kids'], 'stats': 'stdout'},
        models.Settings(
        input=[
            '*.txt',
            '*.csv'],
        output='files/',
        redacts={
            'names': True,
            'genders': False},
        concepts=['kids'],
        stats='stdout'),
        False),
    ({'input': ['*.csv', '*.txt'], 'output': 'files/', 'names': True, 'genders': True, 'concept': ['kids', 'dog'], 'stats': 'stdout'},
        models.Settings(
        input=[
            '*.txt',
            '*.csv'],
        output='files/',
        redacts={
            'names': True,
            'genders': True},
        concepts=['kids'],
        stats='stdout'),
        False),
    ({'input': ['*.csv', '*.txt'], 'output': 'files/', 'names': True, 'concept': ['kids', 'war'], 'stats': 'stdout'},
        models.Settings(
        input=[
            '*.txt',
            '*.csv'],
        output='files/',
        redacts={
            'names': True},
        concepts=['kids', 'war'],
        stats='dummy'),
        False),
]


@pytest.mark.parametrize("input,want,result", test_cases)
def test_settings_dunder_equal_func(input, want, result):
    got = models.Settings.parse(input)

    assert (got == want) is result


def test_settings_dunder_str_func():
    args_in = {
        'input': [
            '*.csv',
            '*.txt'],
        'output': 'files/',
        'names': True,
        'concept': [
            'kids',
            'war'],
        'stats': "stdout"}
    args_out = {
        'input': [
            '*.csv',
            '*.txt'],
        'output': 'files/',
        'redacts': {
            'names': True},
        'concepts': [
            'kids',
            'war'],
        'stats': "stdout"}

    got = models.Settings.parse(args_in)
    want = 'Settings (\n\tinput: {0}\n\toutput: {1}\n\tredacts: {2}\n\tconcepts: {3}\n\tstats: {4}\n)'.format(
        str(args_out['input']), args_out['output'], str(args_out['redacts']), str(args_out['concepts']), args_out['stats'])

    assert str(got) == want
