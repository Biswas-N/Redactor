import spacy

from project1.redactors import name_redactor

BLOCK_CHARACTER = '\u2588'


def redact_pipeline(
        unredacted_txt: str,
        redacts: dict[str, bool]):

    nlp = spacy.load('en_core_web_md')
    doc = nlp(unredacted_txt)

    # if 'names' in redacts and redacts['names'] is True:
    #     doc = name_redactor.redact(doc, BLOCK_CHARACTER)

    return doc.text
