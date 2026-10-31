class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        initial_mul = 1
        left_right = []
        right_left =[]
        curr = 1
        for i in range(0,len(nums)):
            curr*=nums[i]
            left_right.append(curr)
        curr = 1
        for i in range(0,len(nums)):
            curr*=nums[len(nums)-1-i]
            right_left.append(curr)
        results = []
        if len(right_left)>1:
            results.append(right_left[-2])
        else:
            return nums
        for i in range (0,len(nums)-2):
            print(left_right[i])
            print(right_left[len(nums)-3-i])
            results.append(left_right[i]*right_left[len(nums)-3-i])
        results.append(left_right[-2])
        return results
