# 1. Two Sum
#
# https://leetcode.com/problems/two-sum

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            if target - num not in map.values():
                map[i] = num
            else:
                return [i, map[num]]
