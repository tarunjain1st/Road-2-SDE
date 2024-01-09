'''
Question link: https://leetcode.com/problems/leaf-similar-trees/description/

I tackled this problem by performing a depth-first traversal of both binary trees (root1 and root2). During the traversal, 
I identified leaf nodes and stored their values in separate lists (leafs1 and leafs2). Finally, I compared the two lists to check if the leaf sequences are similar.

🧐 Approach Summary:
Traversal: Utilized a recursive depth-first traversal.
Leaf Identification: Identified leaf nodes during traversal.
List Creation: Compiled leaf values into lists for both trees.
Comparison: Checked if the leaf sequences of the two trees are similar.

⏰ Time Complexity: O(n), where n is the total number of nodes in both trees.
🚀 Space Complexity: O(n + h), considering the space for storing leaf values and call stack space (proportional to the height of the tree).

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1 = self.tree_traversal(root1)
        leafs2 = self.tree_traversal(root2)

        if len(leafs1) != len(leafs2): return False
        
        compared_list = [x==y for x,y in zip(leafs1,leafs2)]
        return all(compared_list)

    def is_leaf(self, node):
        return node.left==None and node.right==None
    
    def tree_traversal(self, node):
        if node is None: return []
        if self.is_leaf(node): return [node.val]
        return self.tree_traversal(node.left) + self.tree_traversal(node.right)
