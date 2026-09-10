class Solution(object):
    def maxProfit(self, prices):
        min = prices[0]
        max = prices[0]
        win = 0

        for i in range (0,len(prices)):
            if prices[i]<min:
                min = prices[i]
                max = prices[i]
            if prices[i]>max:
                max = prices[i]
            if win < max-min:
                win = max-min
        
        return win
        """
        :type prices: List[int]
        :rtype: int
        """
        