# URL: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# 116. Populating Next Right Pointers in Each Node

# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

 
# Example 1:

# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:

# Input: root = []
# Output: []
 
# Constraints:

# The number of nodes in the tree is in the range [0, 2**12 - 1].
# -1000 <= Node.val <= 1000
 

# Follow-up:

# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
            
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return root
        
        nodes_q= [(root, 0)]
        
        while nodes_q:
            node, level= nodes_q.pop(0)
            
            if node.left and node.right:
                nodes_q.append((node.left, level+1))
                nodes_q.append((node.right, level+1))
            
            while len(nodes_q)>0 and nodes_q[0][1]== level:
                next_node, next_node_level= nodes_q.pop(0)
                node.next= next_node 
                node= next_node
                if node.left and node.right:
                    nodes_q.append((next_node.left, level+1))
                    nodes_q.append((next_node.right, level+1))
                
        return root