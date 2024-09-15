class Solution:
    def listSum(self , nums):
        hashset = []
        slow = 0
        fast = 0
        sum = 0
       
        i = 0
        while(i < len(nums) and slow != len(nums)):
            if slow != fast:
                sum += nums[fast]
            
            if fast == len(nums)-1:
                hashset.append(sum)
                fast = -1
                slow += 1
                i = -1
                sum = 0
                
            fast += 1
            i+=1
            
        print(hashset)
                
                
            
            
sol = Solution()
num = [1,2,3,4]
sol.listSum(num)



