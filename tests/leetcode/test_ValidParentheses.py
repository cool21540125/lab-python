from leetcode.ValidParentheses import Solution
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
        sol = Solution()
        result = sol.isValid(s)
        assert result == expected
