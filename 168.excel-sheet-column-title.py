# https://leetcode.com/problems/excel-sheet-column-title

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret = []
        while columnNumber > 0:
            columnNumber -= 1
            ret.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26

        return ''.join(ret[::-1])
