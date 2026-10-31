class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        initial_mul = 1
        results=[]
        pos_zeros = []
        for i in range(0, len(nums)):
            if nums[i] != 0:
                initial_mul*=nums[i]
            else:
                pos_zeros.append(i)
        if len(pos_zeros) == 0:
            for i in range(0, len(nums)):
                results.append(initial_mul/nums[i])
        elif len(pos_zeros)==1:
            for i in range(0, len(nums)):
                if pos_zeros[0]==i:
                    results.append(initial_mul)
                else:
                    results.append(0)
        else:
            for i in range(0, len(nums)):
                results.append(0)
        return results


            


