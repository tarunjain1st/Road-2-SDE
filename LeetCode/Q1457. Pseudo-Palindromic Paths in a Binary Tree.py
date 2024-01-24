'''
link: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
Q1457. Pseudo-Palindromic Paths in a Binary Tree

👉 Approach:
Algorithm employs in-order traversal to navigate binary trees, concurrently tracking node occurrences with a frequency dictionary. 
Upon reaching leaf nodes, we check for valid a palindrome paths with current frequency distribution, and using Backtracking it guarantees proper frequency state.



1️⃣ In-Order Traversal: Navigate the binary tree, keeping track of node occurrences using a frequency dictionary.
2️⃣ Leaf Node Check: When reaching a leaf node, verify if the frequency pattern forms a pseudo-palindrome.
3️⃣ Backtracking: Decrement the node contribution before backtracking to maintain traversal integrity.

⏰ TC: O(N), where N is the number of nodes, as each node is visited once
📈 SC: O(N), for the frequency dictionary and recursive stack.
'''

#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
from typing import Optional
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
      
        # Function to check if a frequency dictionary represents a palindrome.
        # Count the number of odd frequencies in the dictionary.
        # At most one odd frequency contribution is allowed in palindromic path. 
        def isPalindrome(path_freq):
            odd = sum(val % 2 for val in path_freq.values())
            return odd <= 1

        def tree_traversal(root, path):
            if not root: return 0 
            
            # Increment contribution of current node in path frequency
            path[root.val] += 1
            
            # Check if leaf node in a path creates palindrome
            if not root.left and not root.right:
                is_valid = isPalindrome(freq)
                freq[root.val] -= 1  # Decrement frequency during backtracking
                return 1 if is_valid else 0
                    
            left_count = tree_traversal(root.left, path)
            right_count = tree_traversal(root.right, path)

            # Decrement contribution of current node in path frequency (Bactrack)
            path[root.val] -= 1

            # Return the sum of counts from left and right subtrees
            return left_count + right_count

        # Example binary tree
        #        1
        #       / \
        #      2   3
        #     / \
        #    4   5
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        root.right = TreeNode(3)

        # Start the in-order traversal with an empty frequency dictionary and return the final count
        return inorder_traversal(root, Counter())

# Example usage
solution = Solution()
result = solution.pseudoPalindromicPaths(root=None)  # Replace None with the root of your binary tree
print(result)
