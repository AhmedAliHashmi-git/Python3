class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val: int):
        while head is not None and head.val == val :
            head = head.next
            
        current = head
        while current is not None and current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head
def printList(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next
    
 
 
List = ListNode(1)
List.next = ListNode(2)
List.next.next = ListNode(3)
List.next.next.next = ListNode(4)
List.next.next.next.next = ListNode(5)
List.next.next.next.next.next = ListNode(2)

sol = Solution()

sol.removeElements(List , 2)
printList(List)

       