# 3248. Snake in Matrix
# https://leetcode.com/problems/snake-in-matrix

from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        directions = {
            "UP": [0, -1],
            "RIGHT": [1, 0],
            "DOWN": [0, 1],
            "LEFT": [-1, 0]
        }

        pos = [0, 0]

        for command in commands:
            direction = directions[command]
            pos = [pos[0]+direction[0], pos[1]+direction[1]]

        return pos[0] + (pos[1]*n)
