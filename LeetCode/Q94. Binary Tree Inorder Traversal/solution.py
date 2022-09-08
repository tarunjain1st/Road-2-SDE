#Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.data =[]
    def inorderTraversal(self, root) -> list[int]:
        if root:
            temp=root
            if temp.left:
                self.inorderTraversal(temp.left)
            self.data.append(temp.val)
            if temp.right:
                self.inorderTraversal(temp.right)

        return self.data
            
        
root = TreeNode(val=1)
root.left = None
root.right = TreeNode(val=2)
root.right.left = TreeNode(val=3)

solve = Solution()
result = solve.inorderTraversal(root)
print(result)