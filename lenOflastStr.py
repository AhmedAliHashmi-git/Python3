class Solution:
      def lengthOfLastString(self,s)->int:
            count = 0
            for i in range(len(s)-1 , 0 ,-1):
                  if s[i] != ' ':
                        count = count + 1
                  if s[i] == ' ' and count > 0:
                        break
                  
            return count
      

s = "   fly me   to   the moon "
solution= Solution()
result = solution.lengthOfLastString(s)
print(result)
                
            














       