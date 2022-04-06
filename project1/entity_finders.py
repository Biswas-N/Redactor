from spacy import Language
from spacy.tokens import Doc, Span
from spacy.matcher import Matcher

import pyap


def names_finder(doc: Doc, nlp: Language) -> list[Span]:
    """Finds the names in a given document

    Parameters
    ----------
    doc     : Raw unredacted document
    nlp     : SpaCy NLP pipeline

    Returns
    -------
    names   : List of names in the form of Spans
    """

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
        [{"ENT_TYPE": "PERSON", "OP": "+"}, {"ORTH": ","},
            {"ENT_TYPE": "PERSON", "OP": "+"}],
        [{"ENT_TYPE": {"IN": ["PERSON", "ORG"]}}, {"ORTH": "'s"}],
        [{"ENT_TYPE": {"IN": ["PERSON", "GPE"]}, "OP": "+"}],
        [{"ENT_TYPE": {"IN": ["NORP", "ORG"]}, "OP": "+"}],
        [{"ENT_TYPE": "NORP"}, {"IS_SPACE": True, "OP": "?"}, {"ORTH": "Grant"}]
    ]

    matcher.add("mNAME", patterns, greedy="LONGEST")

    names = [Span(doc, start, end, label=nlp.vocab[match_id].text)
             for match_id, start, end in matcher(doc)]

    return names


def genders_finder(doc: Doc, nlp: Language) -> list[Span]:
    """Finds the gender-revealing words in a given document

    Parameters
    ----------
    doc     : Raw unredacted document
    nlp     : SpaCy NLP pipeline

    Returns
    -------
    genders : List of gender-revealing words in the form of Spans
    """

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
    """Finds the dates in a given document

    Parameters
    ----------
    doc     : Raw unredacted document
    nlp     : SpaCy NLP pipeline

    Returns
    -------
    dates   : List of dates in the form of Spans
    """

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
    """Finds the phonenumbers in a given document

    Parameters
    ----------
    doc         : Raw unredacted document
    nlp         : SpaCy NLP pipeline

    Returns
    -------
    phonenumbers: List of phonenumbers in the form of Spans
    """

    matcher = Matcher(nlp.vocab)

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


def address_finder(doc: Doc, nlp: Language) -> list[Span]:
    """Finds the addresses in a given document

    Parameters
    ----------
    doc         : Raw unredacted document
    nlp         : SpaCy NLP pipeline

    Returns
    -------
    addresses   : List of addresses in the form of Spans
    """

    matcher = Matcher(nlp.vocab)

    patterns = []
    addresses = pyap.parse(doc.text, country='US')

    for address in addresses:
        start = str(address).split(',')[0].strip().replace('.', '')
        end = str(address).split(',')[-1].strip().replace('.', '')

        # Generating pattern for each address found using pyap
        pattern = [{"ORTH": tok} for tok in start.split(' ')] \
            + [{"TEXT": {"REGEX": r".*"}, "OP": "*"}] \
            + [{"ORTH": tok} for tok in end.split(' ')]
        patterns.append(pattern)

    matcher.add("mADDRESS", patterns, greedy="FIRST")
    addresses = [Span(doc, start, end, label=nlp.vocab[match_id].text)
                 for match_id, start, end in matcher(doc)]

    return addresses


def concept_finder(doc: Doc, nlp: Language, concepts: list[str]) -> list[Span]:
    """Finds the sentences representing given concepts in a given document

    Parameters
    ----------
    doc         : Raw unredacted document
    nlp         : SpaCy NLP pipeline
    concepts    : List of concepts to be redacted

    Returns
    -------
    sentences   : List of sentences in the form of Spans
    """

    concept_words = []
    # Constructing concept related word list
    for concept in concepts:
        token = nlp(concept.lower())[0]
        synonyms = list(set([l.name() for l in token._.wordnet.lemmas()]))

        syn_sets = token._.wordnet.synsets()
        hyponyms = []
        memberholonyms = []
        partholonyms = []
        for synonym in syn_sets:
            for hyponym in [item.lemma_names() for item in synonym.hyponyms()]:
                hyponyms += hyponym
            for memberholonym in [item.lemma_names()
                                  for item in synonym.member_holonyms()]:
                memberholonyms += memberholonym
            for partholonym in [item.lemma_names()
                                for item in synonym.part_holonyms()]:
                partholonyms += partholonym

        concept_words += synonyms + hyponyms + memberholonyms + partholonyms

    redacts = []
    # Finding concepts related sentences in the document
    for sent in doc.sents:
        sent_token_lemmas = [t.lemma_.lower() for t in sent]
        if any(word.replace("_", " ").lower()
               in sent_token_lemmas for word in concept_words):
            redacts.append(Span(doc, sent.start, sent.end, label=f'mCONCEPT'))
        elif any(word.replace("_", " ").lower()
                 in sent.text.lower() for word in concept_words):
            redacts.append(Span(doc, sent.start, sent.end, label=f'mCONCEPT'))

    return redacts
