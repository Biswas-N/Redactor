import spacy
from spacy.tokens import Doc, Span
import re

from project1.entity_finders import names_finder

BLOCK_CHARACTER = '\u2588'


def redact_pipeline(
        unredacted_txt: str,
        redacts: dict[str, bool]) -> str:

    unredacted_txt = re.sub(r' +', ' ', unredacted_txt)

    nlp = spacy.load("en_core_web_md")
    doc = nlp(unredacted_txt)
    with doc.retokenize() as retokenizer:
        for ent in doc.ents:
            retokenizer.merge(ent)

    redactions: list[Span] = []
    if 'names' in redacts and redacts['names'] is True:
        redactions += names_finder(doc, nlp=nlp)

    return redact(doc, redactions)


def redact(doc: Doc, redactions: list[Span]) -> str:
    redacted_text = doc.text
    for ent in redactions:
        redacted_text = redacted_text[:ent.start_char] + BLOCK_CHARACTER * len(
            redacted_text[ent.start_char: ent.end_char]) + redacted_text[ent.end_char:]

    return redacted_text
