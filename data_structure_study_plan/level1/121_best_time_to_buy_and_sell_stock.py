class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0          

        tail = 1
        head = 0
        best_profit = 0
        
        while tail < len(prices):
            profit = prices[tail] - prices[head]
            if profit > 0:
                best_profit = max(profit, best_profit)
            else:
                head = tail
            tail += 1
            
        
        return best_profit