from leetcode.LongestSubstringWithoutRepeatingCharacters import (
    Solution as LongestString,
)
import pytest


class TestlengthOfLongestSubstring:
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("", 0),
            ("pwwkew", 3),
            ("dvdf", 3),
            ("aab", 2),
            (" ", 1),
            ("abcdefa", 6),
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("ababcabcdabc", 4),
        ],
    )
    def test_lengthOfLongestSubstring(self, s, expected):
        longest = LongestString()
        result = longest.lengthOfLongestSubstring(s)
        assert result == expected, f'"{s}" length: {result} != {expected}'
