class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo={}
        def recurse_stairs(left,memo):
            if left in memo:
                return memo[left]
            if left<0:
                memo[left]=0
                return 0
            if left == 0:
                memo[left]=1
                return 1
            memo[left-1]=recurse_stairs(left-1,memo)
            memo[left-2]=recurse_stairs(left-2,memo)
            return memo[left-1]+memo[left-2]
        return recurse_stairs(n,memo)
        
        