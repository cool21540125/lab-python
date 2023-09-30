from leetcode.DesignAddandSearchWordsDataStructure import WordDictionary
import pytest
from typing import List


# https://leetcode.com/problems/design-add-and-search-words-data-structure/
class TestWordDictionary:
    @pytest.mark.parametrize(
        "operation_list, data_list, expected_list",
        [
            (
                [
                    "WordDictionary",
                    "addWord",
                    "addWord",
                    "addWord",
                    "search",
                    "search",
                    "search",
                    "search",
                ],
                [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
                [None, None, None, None, False, True, True, True],
            ),
            (
                [
                    "WordDictionary",
                    "addWord",
                    "addWord",
                    "addWord",
                    "addWord",
                    "search",
                    "search",
                    "addWord",
                    "search",
                    "search",
                    "search",
                    "search",
                    "search",
                    "search",
                ],
                [
                    [],
                    ["at"],
                    ["and"],
                    ["an"],
                    ["add"],
                    ["a"],
                    [".at"],
                    ["bat"],
                    [".at"],
                    ["an."],
                    ["a.d."],
                    ["b."],
                    ["a.d"],
                    ["."],
                ],
                [
                    None,
                    None,
                    None,
                    None,
                    None,
                    False,
                    False,
                    None,
                    True,
                    True,
                    False,
                    False,
                    True,
                    False,
                ],
            ),
        ],
    )
    def test_WordDictionary(
        self, operation_list: List[str], data_list: List[str], expected_list: list[bool]
    ):
        wd = WordDictionary()
        for idx, _ in enumerate(operation_list):
            if operation_list[idx] == "addWord":
                wd.addWord(data_list[idx][0])
            elif operation_list[idx] == "search":
                result = wd.search(data_list[idx][0])
                assert (
                    result == expected_list[idx]
                ), f'"{data_list[idx][0]}" expected should {"" if expected_list[idx] == True else "not "} be found'
            else:
                pass
