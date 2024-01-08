'''
Q938. Range Sum of BST (https://leetcode.com/problems/range-sum-of-bst/description/)
PD: Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Approach
I used basic BST property that inorder traversal of binary search tree is always sorted order, 
so simply do traversal of tree and if node value is in bound of low and high keep adding to final result.

TC: O(n), where n is number of node in tree.
SC: O(h), where h is max height of tree or stack.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans=0
        self.inorder_bst(root, low, high)
        return self.ans
    
    def inorder_bst(self, root, low, high):
        if root==None: return
        self.inorder_bst(root.left, low, high)
        if root.val >= low and root.val<=high:
            self.ans+=root.val
        self.inorder_bst(root.right, low, high)
