
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.visited = set()
        
    def cycle(self , head , index)->bool:
        if head is None:
            return False
        
        if head in self.visited:
            return True
        
        self.visited.add(head)
        
        return self.cycle(head.next , index+1)
        
        
            
    def hasCycle(self, head) -> bool:
        if head is  None:
            return False
        
        return self.cycle(head , 0)
          
        
        

list = ListNode(3)
list.next = ListNode(2)
list.next.next = ListNode(0)
list.next.next.next = ListNode(-4)
list.next.next.next.next = list

sol = Solution()
print(sol.hasCycle(list))
        