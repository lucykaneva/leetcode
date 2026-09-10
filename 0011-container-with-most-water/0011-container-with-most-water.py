class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        curr_height = min(height[j], height[i])
        curr_width = j-i
        max_volume = curr_height * curr_width
        while i < j:
            curr = (j - i) * min(height[i], height[j])
            if curr>max_volume:
                max_volume = curr
            if height[i] < height[j]:
                i+=1
            else:
                j-=1

        return max_volume
        