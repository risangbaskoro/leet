# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)

# See: ./notes/217.contains-duplicate.md
