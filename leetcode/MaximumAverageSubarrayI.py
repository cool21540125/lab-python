from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        matrix = {}
        for ii, item in enumerate(nums):
            if ii <= len(nums) - k:
                matrix[str(ii)] = 0
                for jj in range(ii, ii + k):
                    matrix[str(ii)] += nums[jj]
        max_k = max(matrix, key=matrix.get)
        return matrix[max_k] / k
