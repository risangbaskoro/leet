# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = 0

        while index < len(haystack):
            if haystack[index:].startswith(needle):
                return index

            index += 1

        return -1
