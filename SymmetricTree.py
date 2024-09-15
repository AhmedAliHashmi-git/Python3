class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def check(self, child1, child2) -> bool:
        if not child1 and not child2:
            return True
        if not child1 or not child2:
            return False
        if child1.val != child2.val:
            return False

        left_check = self.check(child1.left, child2.right)
        right_check = self.check(child1.right, child2.left)
        
        if left_check and right_check:
            return True
        else:
            return False

    def isSymmetric(self, root) -> bool:
        if not root:
            return True  
        return self.check(root.left, root.right)


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)

tree.right = TreeNode(2)
tree.right.right = TreeNode(3)
tree.right.left = TreeNode(5)

# Check if the tree is symmetric
sol = Solution()
print(sol.isSymmetric(tree))  



        