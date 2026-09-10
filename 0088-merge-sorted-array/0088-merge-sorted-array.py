class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        pointerNums1=0
        pointerNums2=0
        while pointerNums1 < m+n and pointerNums2 < n:
            if (nums1[pointerNums1]<=nums2[pointerNums2] and (nums1[pointerNums1]!=0 or pointerNums1 < m + pointerNums2-1)):
                pointerNums1=pointerNums1+1
            else:
                self.bubble(nums1, m, pointerNums2, pointerNums1)
                nums1[pointerNums1] = nums2[pointerNums2]
                pointerNums1+=1
                pointerNums2+=1
            print(nums1)

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i]=nums[j]
        nums[j] = temp
    def bubble(self, nums, m, pointer, insertionIndex):
        i = pointer+m
        while i>insertionIndex:
            self.swap(nums,i, i-1)
            i-=1
        
        