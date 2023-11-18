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
            # print(str(nums))
            if nums[y] == val:
                # print(str(nums[y]) + " = " + str(val))
                nums.append(nums[y])
                # print("after append: " + str(nums))
                nums.pop(y)
                # print("after pop: " + str(nums))
            else:
                k += 1
                y += 1
                # print("new k: " + str(k))
        return k