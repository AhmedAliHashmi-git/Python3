class Solution:
    def majorityElement(self, nums) -> int:
        hashset = set()
        res = 0
        result = 0
        
        for i in range(len(nums)):
            if nums[i] not in hashset:
                hashset.add(nums[i])
                val = nums.count(nums[i])
                if val > res:
                    res = val
                    result = nums[i]
                
        
        return result
        
        

sol = Solution()
print(sol.majorityElement([3,2,3]))