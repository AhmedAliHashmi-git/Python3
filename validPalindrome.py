class Solution(object):
    def isPalindrome(self, s):
        s1 = s.lower()
        s2 = ""
        if s is None:
            return True
        for i in s1:
            if(ord(i) >= 97 and ord(i)<=122 or i.isdigit()):
                s2+=i
          
        
        
        left = 0 
        right = len(s2)-1
        
        while(left < right):
            if(s2[left] != s2[right]):
                return False
            left+=1
            right-=1
            
                
        return True
                
        
        
        
sol = Solution()
print(sol.isPalindrome("0P"))
        