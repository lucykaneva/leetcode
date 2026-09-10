class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k>len(nums):
            k = k % len(nums)
        def reverse(nums, start, end):
            i = start
            n = start+end
            while(i < n/2):
                temp = nums[i]
                nums[i] = nums[n-i-1]
                nums[n-i-1]  = temp
                i+=1
        reverse(nums,0, len(nums))
        reverse(nums, 0, k)
        reverse(nums, k, len(nums))


        