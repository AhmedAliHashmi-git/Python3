# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head
        
        
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        
        return False
        


if __name__ == "__main__":
    A = ListNode(1)
    B = ListNode(2)
    C = ListNode(3)
    D = ListNode(4)
    E = ListNode(5)
    
    
    A.next = B
    B.next = C
    C.next = D
    D.next = E
    E.next = None
    
    LL = Solution()
    print(LL.hasCycle(A))
    
    