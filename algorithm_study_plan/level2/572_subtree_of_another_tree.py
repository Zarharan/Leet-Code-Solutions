# URL: https://leetcode.com/problems/subtree-of-another-tree/

# 572. Subtree of Another Tree

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example 1:

# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:

# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

# Constraints:

# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10**4 <= root.val <= 10**4
# -10**4 <= subRoot.val <= 10**4


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        candidate_nodes= self.find_candidates(root, subRoot)
        for node in candidate_nodes:
            if self.compare_trees(node, subRoot):
                return True
            
        return False
        
        
    def compare_trees(self, first_root, second_root):
        first_nodes_q = [first_root]
        second_nodes_q = [second_root]
        
        while len(first_nodes_q)>0 and len(second_nodes_q)>0:
            node1 = first_nodes_q.pop()
            node2 = second_nodes_q.pop()
            if node1.val != node2.val:
                return False
            
            if (not node1.left and node2.left) or (node1.left and not node2.left) or (not node1.right and node2.right) or (node1.right and not node2.right):
                return False
                
            if node1.left:
                first_nodes_q.append(node1.left)
                second_nodes_q.append(node2.left)
            if node1.right:
                first_nodes_q.append(node1.right)
                second_nodes_q.append(node2.right)
        
        return len(first_nodes_q) == len(second_nodes_q)
    
        
    def find_candidates(self, root, target_node):
        if not root or not target_node:
            return []
        
        nodes_q = [root]
        candidate_nodes= []
        
        while len(nodes_q)>0:
            node = nodes_q.pop(0)
            if node.val == target_node.val:
                candidate_nodes.append(node)
                
            if node.left:
                nodes_q.append(node.left)
            if node.right:
                nodes_q.append(node.right)
        
        return candidate_nodes        
        