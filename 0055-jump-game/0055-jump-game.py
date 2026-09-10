class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reachable = 0
        i = 0
        while i < len(nums):
            if max_reachable >= len(nums)-1:
                return True
            if max_reachable < i + nums[i]:
                max_reachable = i+nums[i]
            if max_reachable <= i:
                return False
            i+=1
        return True
            

        