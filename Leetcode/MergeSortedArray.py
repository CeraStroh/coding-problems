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
            for x in range(m):
                if nums1[x] == 0:
                    nums1.pop(x)
            for x in range(n):
                nums1.append(nums2[x])
            nums1.sort() #can't just sort, need to be in non-decreasing order & only pop from end
            for x in range(n):
                nums1.pop(0)