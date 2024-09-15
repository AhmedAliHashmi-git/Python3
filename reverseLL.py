
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        List = []
        if  head is None:
            return None
        temp = head
        while temp is not None:
            List.append(temp.val)
            temp = temp.next
        
        temp = head
            
        List.reverse()
        for i in range(0 , len(List)):
           temp.val = List[i]
           temp = temp.next
        
        temp = head
        
        while temp is not None:
            temp = temp.next
            
            
        return head
               
def printList(List):
    while List is not None:
        print(List.val)
        List = List.next       
           
            
        
        

List = ListNode(1)
List.next = ListNode(2)
# List.next.next = ListNode(3)
# List.next.next.next = ListNode(4)
# List.next.next.next.next = ListNode(5)
sol = Solution()
sol.reverseList(List)
printList(List=List)
        