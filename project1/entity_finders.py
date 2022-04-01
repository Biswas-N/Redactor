from spacy import Language
from spacy.tokens import Doc, Span
from spacy.matcher import Matcher


def names_finder(doc: Doc, nlp: Language) -> list[Span]:
    matcher = Matcher(nlp.vocab)

    titles = [
        "Dr.",
        "Mr.",
        "Ms.",
        "Miss.",
        "Mrs.",
        "Dr",
        "Mr",
        "Ms",
        "Miss",
        "Mrs"]
    patterns = [
        [{"ORTH": {"IN": titles}}, {"IS_SPACE": True, "OP": "?"}, {"ENT_TYPE": "PERSON", "OP": "+"}],
        [{"ENT_TYPE": "PERSON", "OP": "+"}],
        [{"ENT_TYPE": "PERSON", "OP": "+"}, {"ORTH": ","}, {"ENT_TYPE": "PERSON", "OP": "+"}],
        [{"ENT_TYPE": {"IN": ["PERSON", "ORG"]}}, {"ORTH": "'s"}],
        [{"ORTH": "The", "OP": "?"}, {"IS_SPACE": True, "OP": "?"}, {"ENT_TYPE": "ORG", "OP": "+"}],
        [{"ENT_TYPE": {"IN": ["GPE", "NORP"]}}],
        [{"ENT_TYPE": "NORP"}, {"IS_SPACE": True, "OP": "?"}, {"ORTH": "Grant"}]
    ]

    matcher.add("mNAME", patterns, greedy="LONGEST")

    names = [Span(doc, start, end, label=nlp.vocab[match_id].text)
             for match_id, start, end in matcher(doc)]

    return names
