from project1.entity_finders import concept_finder
import pytest
import en_core_web_md
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
import nltk
nltk.download("wordnet")
nltk.download("omw")


@pytest.fixture(scope='module')
def nlp():
    nlp = en_core_web_md.load()
    nlp.add_pipe("spacy_wordnet", after='tagger', config={'lang': nlp.lang})
    return nlp


test_cases = [
    ("""Hi my name is Biswas. Rocky is my dog's names.
    """,
     ["Rocky is my dog's names."]),
    ("""United Kingdom and France fought in World War II. The United Kingdom and France
subsequently declared war on Germany on 3 September.
    """,
     ["United Kingdom and France fought in World War II.",
      "The United Kingdom and France\nsubsequently declared war on Germany on 3 September."]),
    ("""In 1346, Mongols catapult bodies of plague victims over the city walls of Caffa. This is an example of Biological Attack.""",
     ["This is an example of Biological Attack."])
]


@pytest.mark.parametrize("input, concept_sents", test_cases)
def test_names_finder(input: str, concept_sents: list[str], nlp):
    doc = nlp(input)
    got = concept_finder(doc, nlp, concepts=['dog', 'war'])
    print(got)

    assert len(got) == len(concept_sents)
    assert frozenset([tok.text for tok in got]) == frozenset(concept_sents)
