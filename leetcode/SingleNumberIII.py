from typing import List


# https://leetcode.com/problems/single-number-iii/description/
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        resultset = set()
        for item in nums:
            if item not in resultset:
                resultset.add(item)
            else:
                resultset.remove(item)
        return list(resultset)
