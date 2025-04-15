class Solution:
    def twoSum(self, numbers, target):
        p = 0
        q = len(numbers)-1
        for  i in range(len(numbers)):
            if numbers[p] + numbers[q] == target:
                j = p
                k = q
                break
            elif numbers[p] + numbers[q] > target:
                q -= 1
            else:
                p+=1
            
            if i == len(numbers)-1:
                return 0
        
        return j+1 , k+1
                
            
sol = Solution()
# numbers = [2,7,11,15], target = 9
print(sol.twoSum([2,7,11,15] , 9))
        