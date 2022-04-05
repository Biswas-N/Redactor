import pytest
import spacy

from project1.entity_finders import phones_finder


@pytest.fixture(scope='module')
def nlp():
    return spacy.load("en_core_web_md")


test_cases = [
    ("Sample phone number is (800) 353 4940.", ["(800) 353 4940"]),
    ("With US code its +1 (800) 353 4940.", ["+1 (800) 353 4940"]),
    ("Unformated phone numbers are +18003534940 or 8003534940.",
     ["+18003534940", "8003534940"]),
    ("Badly formated phone number is +180 0353 4940.", [])
]


@pytest.mark.parametrize("input, phonenumbers", test_cases)
def test_names_finder(input: str, phonenumbers: list[str], nlp):
    doc = nlp(input)
    got = phones_finder(doc, nlp)
    print(got)

    assert len(got) == len(phonenumbers)
    assert frozenset([tok.text for tok in got]) == frozenset(phonenumbers)
