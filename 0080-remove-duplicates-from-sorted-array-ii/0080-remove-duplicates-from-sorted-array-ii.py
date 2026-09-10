class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        current=0
        j=0
        lastElem=nums[0]
        currentDuplicates = 0
        while(j < len(nums)):
            if (nums[j]==lastElem):
                currentDuplicates+=1
            else:
                lastElem=nums[j]
                currentDuplicates = 1
                
            if(currentDuplicates<=2):
                nums[current]=nums[j]
                current+=1
            j+=1
        return current
        
        