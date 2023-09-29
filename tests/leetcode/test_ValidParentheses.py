from leetcode.ValidParentheses import Solution as ValidParentheses
import pytest


# https://leetcode.com/problems/valid-parentheses/
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
        assert result == expected, f'"{s}" expected to be {expected}, but got {result}'
