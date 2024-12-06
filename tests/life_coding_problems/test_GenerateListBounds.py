from life_coding_problems.GenerateListBounds import Solution
import pytest


class TestListBounds:
    @pytest.mark.parametrize(
        "num, expected",
        [
            (0, []),
            (1, [[0, 1]]),
            (9, [[0, 9]]),
            (10, [[0, 10]]),
            (11, [[0, 10], [10, 11]]),
            (20, [[0, 10], [10, 20]]),
            (21, [[0, 10], [10, 20], [20, 21]]),
        ],
    )
    def test_list_bounds(self, num, expected):
        result = Solution.list_bounds(num)
        assert result == expected, f"{num} 預期為 {expected}, 但卻拿到 {result}"
