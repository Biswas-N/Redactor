from project1.redactors import name_redactor

BLOCK_CHARACTER = '\u2588'


def redact_pipeline(
        unredacted_txt: str,
        redacts: dict[str, bool]) -> str:

    redactions = []
    if 'names' in redacts and redacts['names'] is True:
        redactions += name_redactor.redact(unredacted_txt)

    redacted_txt = redact(unredacted_txt, redactions)
    return redacted_txt


def redact(
        unredacted_txt: str,
        redactions: list[tuple[str, int, int]]) -> str:

    redactions = sorted(redactions, key=lambda r: r[1], reverse=False)
    for r in redactions:
        unredacted_txt = unredacted_txt[:r[1]] + \
            BLOCK_CHARACTER * (r[2] - r[1]) + unredacted_txt[r[2]:]

    return unredacted_txt
