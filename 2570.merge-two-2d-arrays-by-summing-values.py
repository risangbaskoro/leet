# 2570. Merge Two 2D Arrays by Summing Values
# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values

from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ret = []

        while nums1 and nums2:
            idx_i, val_i = nums1[0]
            idx_j, val_j = nums2[0]
            if idx_i == idx_j:
                nums1.pop(0)
                nums2.pop(0)
                ret.append([idx_i, val_i+val_j])
            elif idx_j < idx_i:
                ret.append(nums2.pop(0))
            elif idx_i < idx_j:
                ret.append(nums1.pop(0))

        if nums1:
            ret += nums1
        if nums2:
            ret += nums2

        return ret
