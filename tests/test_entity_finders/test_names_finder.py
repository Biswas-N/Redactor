import pytest
import spacy

from project1.entity_finders import names_finder


@pytest.fixture(scope='module')
def nlp():
    return spacy.load("en_core_web_md")


test_cases = [
    ("My name is Biswas Nandamuri. Also written as Nandamuri Biswas.",
     ["Biswas Nandamuri", "Nandamuri Biswas"]),
    ("I was born in India.", ["India"]),
    ("Currently doing my MS in DSA at The University of Oklahoma.",
     ["The University of Oklahoma", "DSA"]),
    ("Current conflict is between Russia and Ukraine.", ["Russia", "Ukraine"]),
    ("So Russians and Ukrainians are fighting.", ["Russians", "Ukrainians"]),
    ("Joe Biden is the current president of USA.", ["Joe Biden", "USA"]),
    ("Donald Trump and Barak Obama were also the presidents of USA.",
     ["Donald Trump", "Barak Obama", "USA"]),
    ("Our professor is Dr. Christian Grant. And our teaching assistant is Ms Jasmine M. DeHart.", [
     "Dr. Christian Grant", "Ms Jasmine M. DeHart"])
]


@pytest.mark.parametrize("input, names", test_cases)
def test_names_finder(input: str, names: list[str], nlp):
    doc = nlp(input)
    got = names_finder(doc, nlp)

    assert len(got) == len(names)
    assert frozenset([tok.text for tok in got]) == frozenset(names)
