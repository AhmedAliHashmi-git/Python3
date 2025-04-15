from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        # s = sorted(s)
        # t = sorted(t)
        # if s == t:
        #     return True
        # else:
        #     return False
        
        return Counter(s) == Counter(t)


sol = Solution()
print(sol.isAnagram("anagram" , "nagaram"))