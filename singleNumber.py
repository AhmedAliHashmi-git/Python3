# class Solution:
#     def singleNumber(self, nums) -> int:
#         res = 0
#         for n in nums:
#             res = n ^ res
#         return res





class Solution:
    def singleNumber(self, nums) -> int:
        nums.sort()
        hashset = set()
        for i in range(len(nums)-1):
           
            
            if nums[i] == nums[i+1]:
                hashset.add(nums[i])
                
            if nums[i] not in hashset:
                return nums[i]
        return nums[len(nums)-1]
            
        
    
    
    
    
sol = Solution()
print(sol.singleNumber([2,2,1]))