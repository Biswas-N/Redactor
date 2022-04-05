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
        [{"ORTH": {"IN": titles}}, {"IS_SPACE": True, "OP": "?"},
            {"ENT_TYPE": "PERSON", "OP": "+"}],
        [{"ENT_TYPE": "PERSON", "OP": "+"}],
        [{"ENT_TYPE": "PERSON", "OP": "+"}, {"ORTH": ","},
            {"ENT_TYPE": "PERSON", "OP": "+"}],
        [{"ENT_TYPE": {"IN": ["PERSON", "ORG"]}}, {"ORTH": "'s"}],
        [{"ORTH": "The", "OP": "?"}, {"IS_SPACE": True,
                                      "OP": "?"}, {"ENT_TYPE": "ORG", "OP": "+"}],
        [{"ENT_TYPE": {"IN": ["GPE", "NORP"]}}],
        [{"ENT_TYPE": "NORP"}, {"IS_SPACE": True, "OP": "?"}, {"ORTH": "Grant"}]
    ]

    matcher.add("mNAME", patterns, greedy="LONGEST")

    names = [Span(doc, start, end, label=nlp.vocab[match_id].text)
             for match_id, start, end in matcher(doc)]

    return names


def genders_finder(doc: Doc, nlp: Language) -> list[Span]:
    matcher = Matcher(nlp.vocab)

    gender_lemmas = [
        'aunt',
        'babe',
        'boy',
        'boyfriend',
        'brother',
        'dad',
        'daddy',
        'daughter',
        'father',
        'female',
        'him',
        'gal',
        'gentleman',
        'girl',
        'girlfriend',
        'granddaughter',
        'grandma',
        'grandpa',
        'grandson',
        'guy',
        'he',
        'her',
        'hers',
        'herself',
        'himself',
        'his',
        'husband',
        'king',
        'knight',
        'lady',
        'ladylike',
        "ma'am",
        'maiden',
        'male',
        'mama',
        'mamma',
        'man',
        'manful',
        'manlike',
        'manly',
        'miss',
        'mister',
        'mom',
        'mommy',
        'mother',
        'nephew',
        'niece',
        'queen',
        'she',
        'sir',
        'sister',
        'son',
        'stepbrother',
        'stepdaughter',
        'stepfather',
        'stepmother',
        'stepsister',
        'stepson',
        'uncle',
        'wife',
        'woman',
        'womanly',
        'prince',
        'princess']

    patterns = [[{"LOWER": {"IN": gender_lemmas}}]]
    matcher.add("mGENDER", patterns, greedy="LONGEST")
    gender_words = [
        Span(
            doc,
            start,
            end,
            label=nlp.vocab[match_id].text) for match_id,
        start,
        end in matcher(doc)]

    return gender_words
