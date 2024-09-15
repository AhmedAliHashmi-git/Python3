class Solution:
    def reverse(self, x: int) -> int:
        
        
        
        check = False
        
        if x < 0:
            check = True
            x = -x
        
            
        
        val = 0
        
        char = str(x)
        leng = len(char)
        i = 0
        while i != leng:
                
            val = val * 10 + (x%10)
            x = x // 10
            i = i+1
        
        
        if -2**31 <= val <= 2**31 - 1:
            if check:
             return -val
            else:
             return val
        else:
            return 0
            
         
            
        
            

sol = Solution()
print(sol.reverse(-987))