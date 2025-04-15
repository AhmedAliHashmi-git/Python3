class Solution:
    def wordPattern(self, pattern, s) -> bool:
        if len(pattern) != len(s.split()):
            return False
        s2 = s.split()
        if s2.count(s2[0]) == len(s2) and pattern.count(pattern[0]) != len(pattern):
            return False
        if s2.count(s2[0]) != len(s2) and pattern.count(pattern[0]) == len(pattern):
            return False
        l1 = []
        l2 = []
        
        
        
        for i in range(len(pattern)):
            if pattern[i] in l1:
                index_i = l1.index(pattern[i])
                if s2[i] != s2[index_i]:
                     return False
            elif s2[i] in l2:
                return False
            
                
            
            l1.append(pattern[i])
            l2.append(s2[i])
        
        return True
                
                
            

        
        
        
# Input: pattern = "abba", s = "dog cat cat dog"

sol = Solution()
print(sol.wordPattern( "abc","dog cat dog"))