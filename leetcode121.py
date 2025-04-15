class Solution:
    def maxProfit(self, prices) -> int:
        # check = True
        # m = min(prices)
        # for i in range(len(prices)):
        #     if m == prices[-1]:
        #         prices.pop()
        #     else:
        #         break
        #     if not prices:
        #         return 0
        
        
        # m = min(prices)  
        # c = prices.index(m)
        
        # prices[:] = prices[c:]
        # p ,q = 0 , len(prices)-1
        
        # val = 0
        # while q > p:
        #     if prices[p] < prices[q]:
        #         sub =  prices[q] - prices[p]
        #         val = max(sub , val)
        #         q -=1
                
        
        # return val
        
        min = float('inf')
        print(min)


sol = Solution()
print(sol.maxProfit([7,6,5,4,3,2,1]))
        