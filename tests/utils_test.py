# this is the "tests/utils_test.py" file...

from app.utils import to_usd

def test_to_usd():
    #it rounds to two decimal places and has a dollar sign:
    assert to_usd(0.45555) == "$0.46"

    #if large number, should use thousands separator:
    assert to_usd(1234567.89) == "$1,234,567.89"
