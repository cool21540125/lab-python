from leetcode.ValidParentheses import Solution as ValidParentheses
import pytest


class TestValidParentheses:
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
            ("{[]}", True),
            ("((", False),
            ("[", False),
            ("][", False),
            ("(){}}{", False),
            ("{}[{}]((){})(){}", True),
        ],
    )
    def test_isValid(self, s, expected):
        sol = ValidParentheses()
        result = sol.isValid(s)
        assert result == expected
