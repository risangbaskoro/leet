# 1. Two Sum
# https://leetcode.com/problems/two-sum

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            res = target - num
            if res not in map:
                map[num] = i
            else:
                return [i, map[res]]
