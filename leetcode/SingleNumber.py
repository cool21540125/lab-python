from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        for _, num in enumerate(nums):
            if nums.count(num) == 1:
                return num
