import pytest
import spacy

from project1.entity_finders import address_finder


@pytest.fixture(scope='module')
def nlp():
    return spacy.load("en_core_web_md")


test_cases = [("OU address is 660 Parrington Oval, Norman, OK 73019.",
               ["660 Parrington Oval, Norman, OK 73019"]),
              ("OU address with newline in it is 660 Parrington Oval\nNorman, OK 73019",
               ["660 Parrington Oval\nNorman, OK 73019"]),
              ("660 Parrington Oval, Norman, OK 73019 is OU and, 1263 Lincoln Dr\nCarbondale\nIL 62901 is SIU",
               ["660 Parrington Oval, Norman, OK 73019",
                "1263 Lincoln Dr\nCarbondale\nIL 62901"]),
              ("Non US address sample is Plenty Rd &, Kingsbury Dr, Bundoora VIC 3086, Australia.",
               []),
              ("Non US address sample is Plenty Rd &, Kingsbury Dr, Bundoora VIC 3086.",
               [])]


@pytest.mark.parametrize("input, address", test_cases)
def test_names_finder(input: str, address: list[str], nlp):
    doc = nlp(input)
    got = address_finder(doc, nlp)
    print(got)

    assert len(got) == len(address)
    assert frozenset([tok.text for tok in got]) == frozenset(address)
