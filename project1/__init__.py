from project1 import entity_finders
from typing import Tuple
import re
import spacy
import en_core_web_md
from spacy.tokens import Doc, Span
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
import nltk
nltk.download("wordnet", quiet=True)
nltk.download("omw", quiet=True)


BLOCK_CHARACTER = '\u2588'


def redact_pipeline(
        unredacted_txt: str,
        redacts: dict[str, bool],
        concepts: list[str]) -> Tuple[str, str]:

    unredacted_txt = re.sub(r' +', ' ', unredacted_txt)

    nlp = en_core_web_md.load()

    doc = nlp(unredacted_txt)

    redactions: list[Span] = []
    if 'address' in redacts and redacts['address'] is True:
        redactions += entity_finders.address_finder(doc, nlp=nlp)

    if 'names' in redacts and redacts['names'] is True:
        redactions += entity_finders.names_finder(doc, nlp=nlp)

    if 'genders' in redacts and redacts['genders'] is True:
        redactions += entity_finders.genders_finder(doc, nlp=nlp)

    if 'dates' in redacts and redacts['dates'] is True:
        redactions += entity_finders.dates_finder(doc, nlp=nlp)

    if 'phones' in redacts and redacts['phones'] is True:
        redactions += entity_finders.phones_finder(doc, nlp=nlp)


    if len(concepts) > 0:
        nlp = spacy.load("en_core_web_md")
        nlp.add_pipe(
            "spacy_wordnet",
            after='tagger',
            config={
                'lang': nlp.lang})

        doc = nlp(unredacted_txt)
        with doc.retokenize() as retokenizer:
            for ent in doc.ents:
                retokenizer.merge(ent)
        redactions += entity_finders.concept_finder(
            doc, nlp=nlp, concepts=concepts)

    return redact(doc, redactions), get_stats(doc, redactions)


def redact(doc: Doc, redactions: list[Span]) -> str:
    redacted_text = doc.text
    for ent in redactions:
        redacted_text = redacted_text[:ent.start_char] + BLOCK_CHARACTER * len(
            redacted_text[ent.start_char: ent.end_char]) + redacted_text[ent.end_char:]

    return redacted_text


def get_stats(doc: Doc, redactions: list[Span]) -> str:
    stats_txt_arr = []

    redact_types = [
        "mNAME",
        "mGENDER",
        "mDATE",
        "mPHONENUM",
        "mADDRESS",
        "mCONCEPT"]

    for redact_type in redact_types:
        redacts_for_type = [(r.start_char, r.end_char)
                            for r in redactions if r.label_ == redact_type]
        stats_txt_arr.append(
            f"{redact_type[1:]}: {len(redacts_for_type)} redactions")

        for start, end in sorted(redacts_for_type):
            stats_txt_arr.append(
                f"\tStart: {start}, End: {end} => {doc.text[start: end]}")

    return "\n".join(stats_txt_arr)
