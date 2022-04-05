import pytest
import spacy

from project1.entity_finders import dates_finder


@pytest.fixture(scope='module')
def nlp():
    return spacy.load("en_core_web_md")


test_cases = [("He was born on 3rd February, 2001",
               ["3rd February, 2001"]),
              ("Which can also be written as 3/2/2001 or 02/03/2001 or 02/03/01",
               ["3/2/2001",
                "02/03/2001",
                "02/03/01"]),
              ("In short Feb 3rd 2001 as well",
               ["Feb 3rd 2001"])]


@pytest.mark.parametrize("input, dates", test_cases)
def test_names_finder(input: str, dates: list[str], nlp):
    doc = nlp(input)
    got = dates_finder(doc, nlp)
    print(got)

    assert len(got) == len(dates)
    assert frozenset([tok.text for tok in got]) == frozenset(dates)
