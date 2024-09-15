class Solution:
    def containsDuplicate(self, nums)->bool:
        # nums.sort()
        # check = False
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         check = True
        #         break
        # return check    
        
        hashset = set()
        
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        
        return False
                
        
        
        

sol = Solution()
num = [1,3,4,2,1]
print(sol.containsDuplicate(num))
