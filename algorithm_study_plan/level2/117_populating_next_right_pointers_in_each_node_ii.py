# URL: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# 117. Populating Next Right Pointers in Each Node II

# Given a binary tree

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Example 1:

# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:

# Input: root = []
# Output: []

# Constraints:

# The number of nodes in the tree is in the range [0, 6000].
# -100 <= Node.val <= 100
 
# Follow-up:

# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

from collections import defaultdict
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
    def connect(self, root: 'Node') -> 'Node':
        
        return self.iterative_solution(root)
        
        # return self.recursive_solution(root)
        
    
    def iterative_solution(self, root):
        if not root:
            return root
        
        level_q = []
        level_q.append(root)
        
        while len(level_q)>0:
            rightest_node = None
            level_nodes_no = len(level_q)
            for idx in range(level_nodes_no):
                target_node= level_q.pop(0)
                target_node.next = rightest_node
                rightest_node = target_node
                
                if target_node.right:
                    level_q.append(target_node.right)
                    
                if target_node.left:
                    level_q.append(target_node.left)
                    
        return root
        
    
    def recursive_solution(self, root):
        if not root:
            return root
        
        self.levels = defaultdict(list)
        self.level_order(root, 1)
        
        for lst in self.levels.values():
            for idx in range(len(lst) -1):
                lst[idx].next = lst[idx + 1]
        
        return root
    
    
    def level_order(self, node, level):
        if not node:
            return
        
        self.levels[level].append(node)
        
        if node.left:
            self.level_order(node.left, level + 1)
        if node.right:
            self.level_order(node.right, level + 1)