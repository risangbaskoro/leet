# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/

from collections import deque
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = deque()
        ileft, iright = 0, len(nums) - 1

        while ileft <= iright:
            left, right = abs(nums[ileft]), abs(nums[iright])
            if left > right:
                answer.appendleft(left**2)
                ileft += 1
            else:
                answer.appendleft(right**2)
                iright -= 1

        return list(answer)
