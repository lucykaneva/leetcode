class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_length = 0
        start = 0
        end = 0
        current_sum = 0
        j = start
        while start<=end and end< len(nums):
            current_sum += nums[end]
            while current_sum>=target:
                if end-start+1 < min_length or min_length==0:
                    min_length = end-start+1
                start+=1
                current_sum -= nums[start-1]
            end+=1

        return min_length