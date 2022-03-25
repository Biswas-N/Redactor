import pytest
from project1 import redact_pipeline


@pytest.mark.filterwarnings(
    "ignore:SelectableGroups dict interface is deprecated:DeprecationWarning")
def test_pipeline():
    unredacted_txt = "Dr. Christian Grant is our professor and Jasmine DeHart is our TA."

    got = redact_pipeline(unredacted_txt, {'names': True})
    want = "███████████████ is out professor and ██████████████ is our TA."

    assert got != want
