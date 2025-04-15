class Solution:
    def threeSum(self, nums):
        nums.sort()
        
        # print(nums)
        s = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            p = i+1
            q = len(nums)-1
            while p < q:
                sum = nums[i]+nums[p]+nums[q]
                if sum > 0:
                    q -= 1
                elif sum < 0:
                    p += 1
                else:
                    s.add((nums[i], nums[p], nums[q]))  
                    
                    while p < q and nums[p] == nums[p + 1]:
                        p += 1
                    while p < q and nums[q] == nums[q - 1]:
                        q -= 1
                    
                    p += 1
                    q -= 1
                
        
        return list(s)
                    
                
        
    




sol = Solution()

# [-4, -1, -1, 0, 1, 2]

# print(sol.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))
print(sol.threeSum([-1,0,1,2,-1,-4]))