import spacy


def redact(unredacted_txt: str):
    nlp = spacy.load('en_core_web_md')

    titles = ["Dr.", "Mr.", "Ms.", "Miss.", "Mrs.", ""]
    ruler = nlp.add_pipe(
        "entity_ruler", after='ner', config={
            "overwrite_ents": True})
    patterns = [{"label": "NAME",
                 "pattern": [{"ORTH": {"IN": titles},
                              "OP": "?"},
                             {"IS_SPACE": True,
                              "OP": "?"},
                             {"ENT_TYPE": "PERSON",
                              "OP": "+"}]},
                {"label": "NAME",
                 "pattern": [{"ENT_TYPE": "PERSON",
                              "OP": "+"},
                             {"ORTH": ","},
                             {"ENT_TYPE": "PERSON",
                              "OP": "+"}]}]
    ruler.add_patterns(patterns)

    doc = nlp(unredacted_txt)

    return [(ent.label_, ent.start_char, ent.end_char)
            for ent in doc.ents if ent.label_ in ('NAME')]
