
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self) -> None:
        self.List = []
         
    def countNodes(self, root) -> int:

           if root is None:
             return 0
           self.List.append(root.val)
           if root.left is not None:
               self.countNodes(root=root.left)
               
           if root.right is not None:
                self.countNodes(root=root.right)
                
           length = len(self.List)
           return length
    
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.right = TreeNode(5)
tree.left.left = TreeNode(4)

tree.right=TreeNode(3)
tree.right.left = TreeNode(6)

sol = Solution()
print(sol.countNodes(tree))