# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []

        while matrix:
            # Step 1: Add first row, forward
            ret += matrix.pop(0)

            # Step 2: Add last column, forward
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop(-1))

            # Step 3: Add last row, backward
            if matrix and matrix[0]:
                ret += matrix.pop(-1)[::-1]

            # Step 4: Add first column, backward
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret
