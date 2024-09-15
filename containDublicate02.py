class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        window = set()
        L = 0
        for R in range(len(nums)):
            if R-L > k:
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                return True
            window.add(nums[R])
        
        return False                


sol = Solution()
print(sol.containsNearbyDuplicate([1,2,3,4,5,6,8,7,9,0,1] , 3))
