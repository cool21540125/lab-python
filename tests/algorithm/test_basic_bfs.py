from algorithm.basic_bfs import bfs
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
            ["A", "B", "C", "D", "E", "F"],
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
            ["B", "A", "C", "D", "E", "F"],
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
            ["C", "A", "B", "D", "E", "F"],
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
            "D",
            ["D", "B", "C", "E", "F", "A"],
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
            "E",
            ["E", "C", "D", "A", "B", "F"],
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
            "F",
            ["F", "D", "B", "C", "E", "A"],
        ),
    ],
)
def test_basic_bfs(graph: Mapping, start: str, expected: List):
    result = bfs(graph, start)
    assert (
        result == expected
    ), f"Start from: '{start}', Expected: {expected}, but got {result}"
