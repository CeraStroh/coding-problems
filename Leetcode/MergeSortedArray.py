# Pop n numer of 0's at end of nums1, merge 2 non-decreasing arrays, sort
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) != 0:
            for x in range(n):
                nums1.pop(len(nums1)-1)
            for x in range(n):
                nums1.append(nums2[x])
            nums1.sort()
            