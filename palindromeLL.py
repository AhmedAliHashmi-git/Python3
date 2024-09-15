\
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        if head is None:
            return False
        List = []
        temp = head
        while(temp is not None):
            List.append(temp.val)
            temp = temp.next
        
        List2 = []
        for i in range(len(List)-1 , -1 , -1):
            List2.append(List[i])
        return List2 == List


list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(2)
list.next.next.next = ListNode(1)
sol = Solution()
print(sol.isPalindrome(list))