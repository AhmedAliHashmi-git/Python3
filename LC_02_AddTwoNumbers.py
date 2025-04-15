# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        curr1 = l1
        curr2 = l2
        dummy = ListNode(0)
        curr3 = dummy
        
        
        while curr1 or curr2:
            
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            new_node = ListNode(val1 + val2)
            
            new_node = ListNode(curr1.val + curr2.val)
            
            if new_node.val >= 10:
                Q = new_node.val % new_node.val
                R = new_node.val // new_node.val
                
                new_node.val = R
                if new_node.next:
                    new_node.next.val += Q
                else:
                    new_node = ListNode(Q) 
                
            curr3.next = new_node
            curr3 = curr3.next
            
            
            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next
            
            
        res = dummy.next
        while res:
            print(res.val)
            res = res.next
        
        
        

if __name__ == "__main__":
    
    A = ListNode(2)
    B = ListNode(4)
    C = ListNode(3)
    
    A.next = B
    B.next = C
    C.next = None
    

    D = ListNode(5)
    E = ListNode(6)
    F = ListNode(4)
    
    D.next = E
    E.next = F
    F.next = None
    
    sol = Solution()
    
    sol.addTwoNumbers(A , D)