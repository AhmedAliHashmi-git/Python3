class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None 

        return self.intoBST(nums, 0, len(nums) - 1)
        
    def intoBST(self, nums, start, end):
        if start > end:
            return None  

        mid = (start + end) // 2
        
        root = TreeNode(nums[mid])
        
        root.left = self.intoBST(nums, start, mid - 1)
        root.right = self.intoBST(nums, mid + 1, end)
        
        return root

def print_inorder(root):
    if root:
        print(root.val, end=' ')
        print_inorder(root.left)
        print_inorder(root.right)

sol = Solution()
nums = [-10, -3, 0, 5, 9]
bst_root = sol.sortedArrayToBST(nums)
print_inorder(bst_root)  
