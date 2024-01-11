'''
Link: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor
# Intuition
Our goal is to find maximum value of parent with it's ancestor, so we need to keep track of minimum and maximum node of ancestor for each parent.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
I approached the problem by first performing a depth-first traversal of the binary tree, The goal was to getting minimum and maximum value of Ancestor for each node, during tree_traversal we compares the current node’s value with its left and right children’s values, updating the local_min and local_max values accordingly. Finally, it calculates the maximum difference between the current node’s value and the local_min or local_max and updates the max_val attribute.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
⏰ TC: O(n), where n is the total number of nodes in tree.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
🚀 SC: O(h), where h is max height of stack for recursion.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
'''

# Code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_val = float('-inf')
        self.tree_traversal(root) 
        return self.max_val
    
    def tree_traversal(self, root):
        local_min, local_max = root.val, root.val

        if root.left:
            left_min, left_max = self.tree_traversal(root.left)   
            local_min = min(local_min, left_min) 
            local_max = max(local_max, left_max) 
        if root.right:
            right_min, right_max = self.tree_traversal(root.right)
            local_min = min(local_min, right_min) 
            local_max = max(local_max, right_max)
        
        self.max_val = max(self.max_val, abs(root.val-local_min), abs(root.val-local_max))
        return local_min, local_max

```
