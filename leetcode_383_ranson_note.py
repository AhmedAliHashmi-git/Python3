class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        split_list1 = list(ransomNote)
        split_list2 = list(magazine)
        
        for i in split_list1:
            if i in split_list2:
                split_list2.remove(i)  
            else:
                return False  
        return True
        
        

sol = Solution()
print(sol.canConstruct("aa" , "ab"))