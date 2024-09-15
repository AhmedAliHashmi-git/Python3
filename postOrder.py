
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.list = []
        
    def postorderTraversal(self, root):
        if root is None:
            return self.list
    
        
        
        
        if  root.left is not None:
            self.postorderTraversal(root.left)
        
        if root.right is not None:
            self.postorderTraversal(root.right)
        
        self.list.append(root.val)
            
        return self.list
        
        
        


tree = TreeNode(1)
tree.right = TreeNode(2 , None , tree.right)
tree.right.left = TreeNode(3 , None,tree.right.left)
sol = Solution()
print(sol.postorderTraversal(tree))
        