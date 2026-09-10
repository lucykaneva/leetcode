class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_right=[]
        right_left=[]
        multiple = 1
        for i in range(0,len(nums)-1):
            multiple *= nums[i]
            left_right.append(multiple)
        
        multiple=1
        for i in range(len(nums)-1,0,-1):
            multiple *= nums[i]
            right_left.append(multiple)
       
        answer=[right_left[len(right_left)-1]]
        for i in range(0, len(right_left)-1):
            answer.append(left_right[i]*right_left[len(left_right)-2-i])
        answer.append(left_right[len(left_right)-1])
        return answer
