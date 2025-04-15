from collections import Counter

class Solution:
    def groupAnagrams(self , strs):
        
        l = []
        first = True
        for i in strs: #------> O(n)
            
            check = False  #---------> O(1)
            
            if strs.index(i) == 0 and first: #----------> O(1)
                l.append([i]) #----------------O(1)
                first = False
                
            else:# -------------------->O(1)
                for j in range(len(l)): #----------------->O(l)
                    if sorted(i) == sorted(l[j][0]): #---------------------->O(1)
                        l[j].append(i)#----------------------->O(l)
                        check = True
                        break   
                if not check:
                    l.append([i])
            
        
        
        return l
            
            
        
                        
            
                
sol = Solution()
print(sol.groupAnagrams(["",""]))

# ["eat","tea","tan","ate","nat","bat"]