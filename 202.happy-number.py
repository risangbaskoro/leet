# 202. Happy Number
# https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        while len(str(n)) != 1:
            n = sum([int(x)**2 for x in str(n)])

        return n == 1 or n == 7

# Notes:
# Remember that we must include 7 as
# - 7^2 = 49
# - 4^2 + 9^2 = 97
# - 9^2 + 7^2 = 130
# - 1^2 + 3^2 + 0^2 = 10
# - 1^2 + 0^2 = 1
