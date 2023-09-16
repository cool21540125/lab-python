from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for idx in range(len(nums)):
            remaining = target - nums[idx]
            if remaining in numMap:
                return [numMap[remaining], idx]
            numMap[nums[idx]] = idx
