class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_reachable = 0
        current_jump_end = 0
        num_jumps = 0
        min_num_jumps = 0
        for i in range(0,len(nums)-1):
            if max_reachable < nums[i] + i:
                max_reachable = nums[i] + i
            if max_reachable == len(nums)-1:
                return num_jumps+1
            if i==current_jump_end:
                num_jumps+=1
                current_jump_end = max_reachable
        return num_jumps