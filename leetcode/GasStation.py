from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        power = 0
        begin_at = 0
        for current in range(len(gas)):
            power += gas[current] - cost[current]
            if power < 0:
                power = 0
                begin_at = current + 1
        return begin_at
