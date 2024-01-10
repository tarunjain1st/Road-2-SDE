'''
Q2385. Amount of Time for Binary Tree to Be Infected

Approach:
I approached the problem by first performing a depth-first traversal of the binary tree, establishing relationships between nodes. 
The goal was to record the parent and children of each node in a dictionary. Subsequently, a breadth-first search (BFS) was employed to calculate the time it takes to traverse the tree from a specified starting node. 
The count of levels during BFS serves as an indicator of the time required to explore the entire tree from the given starting point.

⏰ TC: O(n), where n is the total number of nodes in both trees.
🚀 SC: O(n), for storing nodes and it neighbors relations.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.node_relations = {}
        self.tree_traversal(root,None)
        queue, visited, ans = deque(), set(), -1
        visited.add(start)
        queue.append(start)
        while queue:
            size = len(queue)
            while size:
                x = queue.popleft()
                visited.add(x)
                for node in self.node_relations[x]:
                    if node and node not in visited:
                        queue.append(node)
                size-=1
            ans+=1
        return ans

    def tree_traversal(self, root, parent):
        links = [parent,None,None] # nodes -> parent, left, right
        if root.left:
            links[1]=root.left.val
            self.tree_traversal(root.left, root.val)
        if root.right:
            links[2]=root.right.val
            self.tree_traversal(root.right, root.val)
        self.node_relations[root.val] = links
