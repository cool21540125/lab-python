from leetcode.LongestSubstringWithoutRepeatingCharacters import Solution
import pytest


class TestlengthOfLongestSubstring:
    @pytest.mark.parametrize(
        "s, expected", [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3)]
    )
    def test_lengthOfLongestSubstring(self, s, expected):
        s = Solution()
        result = s.lengthOfLongestSubstring(s)
        assert result == expected
