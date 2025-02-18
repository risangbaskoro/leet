# 3248. Snake in Matrix
# https://leetcode.com/problems/snake-in-matrix

from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        directions = {
            "UP": [0, -n],
            "RIGHT": [1, 0],
            "DOWN": [0, n],
            "LEFT": [-1, 0]
        }

        pos = 0

        for command in commands:
            pos += sum(directions[command])

        return pos

# See: ./notes/3248.snake-in-matrix.md
