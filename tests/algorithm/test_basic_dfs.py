from algorithm.basic_dfs import dfs
import pytest
from typing import Mapping, List


@pytest.mark.parametrize(
    "graph, start, expected",
    [
        (
            {
                "A": ["B", "C"],
                "B": ["A", "C", "D"],
                "C": ["A", "B", "D", "E"],
                "D": ["B", "C", "E", "F"],
                "E": ["C", "D"],
                "F": ["D"],
            },
            "A",
            ["A", "C", "E", "D", "F", "B"],
        ),
        (
            {
                "A": ["B", "C"],
                "B": ["A", "C", "D"],
                "C": ["A", "B", "D", "E"],
                "D": ["B", "C", "E", "F"],
                "E": ["C", "D"],
                "F": ["D"],
            },
            "B",
            ["B", "D", "F", "E", "C", "A"],
        ),
        (
            {
                "A": ["B", "C"],
                "B": ["A", "C", "D"],
                "C": ["A", "B", "D", "E"],
                "D": ["B", "C", "E", "F"],
                "E": ["C", "D"],
                "F": ["D"],
            },
            "C",
            ["C", "E", "D", "F", "B", "A"],
        ),
    ],
)
def test_basic_dfs(graph: Mapping, start: str, expected: List):
    result = dfs(graph, start)
    assert (
        result == expected
    ), f"Start from: '{start}', Expected: {expected}, but got {result}"
