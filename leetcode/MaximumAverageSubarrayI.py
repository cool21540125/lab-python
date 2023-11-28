from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])

        for idx in range(k, len(nums)):
            currSum += nums[idx] - nums[idx - k]
            maxSum = max(maxSum, currSum)
        return maxSum / k
