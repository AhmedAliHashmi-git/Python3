
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.list = []
        
    def preorderTraversal(self, root):
        if root is None:
            return self.list
    
        
        self.list.append(root.val)
        
        if  root.left is not None:
            self.preorderTraversal(root.left)
        
        if root.right is not None:
            self.preorderTraversal(root.right)
            
        return self.list
        
        
        


tree = TreeNode(1)
tree.right = TreeNode(2 , None , tree.right)
tree.right.left = TreeNode(3 , None,tree.right.left)
sol = Solution()
print(sol.preorderTraversal(tree))
        