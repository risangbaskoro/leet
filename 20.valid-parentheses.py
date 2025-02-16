# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        p = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        d = []

        for char in s:
            if char in p.values():
                d.append(char)
            elif char in p.keys():
                if not d or p[char] != d.pop():
                    return False

        return not d
