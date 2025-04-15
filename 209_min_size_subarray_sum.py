class Solution:
    def minSubArrayLen(self, target, nums):
        l = 0
        sumval = 0
        minn = float('inf')
        for r in range(len(nums)):
            
            sumval = sumval + nums[r]
            
            while sumval >= target:
                minn = min(minn ,(r-l)+1)
                sumval -= nums[l]
                l = l+1
                
                
        return minn if minn != float('inf') else 0
    

sol = Solution()
print(sol.minSubArrayLen(15, [1,2,3,4,5]))