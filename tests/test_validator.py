from nightwing.core.validator import validate_claim


def test_validate_claim_true():
    assert validate_claim("abc", "zzz abc zzz") is True
