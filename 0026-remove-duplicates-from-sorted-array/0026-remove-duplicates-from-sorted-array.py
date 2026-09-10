class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicates = 0
        unique=0
        seen = set()
        i = 0
        j = 1

        while(i<len(nums) and j<len(nums)):
            if nums[i] == nums[j]:
                j+=1
            else:
                i+=1
                if i+1<len(nums):
                    nums[i] = nums[j]    
        return i+1       
            

        