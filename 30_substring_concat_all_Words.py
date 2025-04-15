from collections import Counter

class Solution:
    def findSubstring(self, s, words) :
        l1 = len(words[0])
        word2 = "".join(words)
        w2 = Counter(word2)
        l = 0
        listt = []
        
        for r in range(len(s)):
            if (r-l)+1 == len(word2):
                if Counter(s[l:r+1]) == w2:
                    listt.append(l)
                    l = l+l1
                else:
                    l = l+l1
            
        return listt 
                

sol = Solution()
print(sol.findSubstring("ling mind rabo ofoo owin gdin gbar rwin gmon keyp ound cake " ,["fooo","barr","wing","ding","wing"]))