# If value equals val, move it to end of array & count number of values that equal val
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        y = 0
        for x in range(len(nums)):
            if nums[y] == val:
                nums.append(nums[y])
                nums.pop(y)
            else:
                k += 1
                y += 1
        return k