class TreeNode:
    def __init__(self , val=0 ,left=None , right=None) :
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def dept(self, node , level):
        if node is None:
            return level-1
        if not node.left and not node.right:
            return level
        left = self.dept(node.left , level+1)
        right = self.dept(node.right , level+1)
        return max(left , right)

    def maxDept(self,root):
        if not root:
            return 0
        
        if root.left is None and root.right is not None:
            return 1
        
        return self.dept(root,1)


node = TreeNode(3)
node.left = TreeNode(9 , node.left,None)
node.right = TreeNode(9 , None,node.right)
node.right.left = TreeNode(9 , None,node.right.left)
node.right.right = TreeNode(9 , None,node.right.right)
node.right.right.right = TreeNode(9 , None,node.right.right.right)
sol = Solution()
print(sol.maxDept(node))



