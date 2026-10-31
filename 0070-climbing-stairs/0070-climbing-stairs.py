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
            result = recurse_stairs(left - 1, memo) + recurse_stairs(left - 2, memo)
            memo[left] = result
            return result
        return recurse_stairs(n,memo)
        
        