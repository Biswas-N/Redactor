import pytest
import spacy

from project1.entity_finders import genders_finder


@pytest.fixture(scope='module')
def nlp():
    return spacy.load("en_core_web_md")


test_cases = [
    ("He was born in the US", ["He"]), ("He is my brother and the other man is my father", [
        "He", "brother", "man", "father"]), ("She was the princess to her father. Now she is a queen.", [
            "She", "princess", "her", "father", "she", "queen"])]


@pytest.mark.parametrize("input, genders", test_cases)
def test_names_finder(input: str, genders: list[str], nlp):
    doc = nlp(input)
    got = genders_finder(doc, nlp)
    # print(got)

    assert len(got) == len(genders)
    assert frozenset([tok.text for tok in got]) == frozenset(genders)
