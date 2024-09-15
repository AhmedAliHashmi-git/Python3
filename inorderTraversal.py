class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        temp = root
        if root is None:
            return 

        if temp.left is not None:
            self.inorderTraversal(temp.left)
        
        print(temp.val)

        if temp.right is not None:
            self.inorderTraversal(temp.right)


root = TreeNode(1)
root.right = TreeNode(2, None, root.right)
root.left = TreeNode(3, root.left, None)

sol = Solution()
sol.inorderTraversal(root)
