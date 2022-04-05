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


def dates_finder(doc: Doc, nlp: Language) -> list[Span]:
    matcher = Matcher(nlp.vocab)

    patterns = [
        [{"ENT_TYPE": "DATE", "OP": "+"}],
        [{"TEXT": {"REGEX": "[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}"}}],
        [{"TEXT": {"REGEX": "[0-9]{1,2}/[0-9]{1,2}/[0-9]{2}"}}]
    ]
    matcher.add("mDATE", patterns, greedy="LONGEST")
    dates = [Span(doc, start, end, label=nlp.vocab[match_id].text)
             for match_id, start, end in matcher(doc)]

    return dates


def phones_finder(doc: Doc, nlp: Language) -> list[Span]:
    matcher = Matcher(nlp.vocab)

    # https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s02.html
    patterns = [
        [
            {"ORTH": "+1", "OP": "?"},
            {"ORTH": "(", "OP": "?"},
            {"TEXT": {"REGEX": "[2-9][0-8][0-9]"}},
            {"ORTH": ")", "OP": "?"},
            {"TEXT": {"REGEX": r"[-.● ]"}, "OP": "?"},
            {"TEXT": {"REGEX": "[2-9][0-9]{2}"}},
            {"TEXT": {"REGEX": r"[-.● ]"}, "OP": "?"},
            {"TEXT": {"REGEX": "[0-9]{4}"}}
        ],
        [
            {"TEXT": {"REGEX": "[2-9][0-8][0-9][2-9][0-9]{2}[0-9]{4}"}}
        ]
    ]

    matcher.add("mPHONENUM", patterns, greedy="LONGEST")
    phone_numbers = [
        Span(
            doc,
            start,
            end,
            label=nlp.vocab[match_id].text) for match_id,
        start,
        end in matcher(doc)]

    return phone_numbers

