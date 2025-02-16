# https://leetcode.com/problems/jewels-and-stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ret = 0

        for stone in stones:
            for jewel in jewels:
                if jewel == stone:
                    ret += 1

        return ret
