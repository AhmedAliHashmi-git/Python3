class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicate(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        current = head

        while current and current.next:
            if current.val == current.next.val:
                temp = current.next
                current.next = current.next.next
                del temp
            else:
                current = current.next

        return head


def printList(node: ListNode):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()  # For a new line after printing the list


if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(1)
    node.next.next = ListNode(2)
    sol = Solution()
    sol.deleteDuplicate(node)
    printList(node)
