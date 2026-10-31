class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        def recurse_coins(left,coins,memo):
            if left in memo:
                return memo[left]
            if left == 0:
                return 0
            if left<0:
                return float('inf')
            best = float('inf')
            for i in range(len(coins)):
               best = min(best,1 + recurse_coins(left-coins[i],coins,memo))
            memo[left] = best
            return best
        ans = recurse_coins(amount,coins,{})
        return -1 if ans == float('inf') else ans

        