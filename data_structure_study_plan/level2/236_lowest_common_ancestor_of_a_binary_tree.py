# URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# 236. Lowest Common Ancestor of a Binary Tree

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [1,2], p = 1, q = 2
# Output: 1 

# Constraints:

# The number of nodes in the tree is in the range [2, 10**5].
# -10**9 <= Node.val <= 10**9
# All Node.val are unique.
# p != q
# p and q will exist in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    
    # Runtime: 90 ms, faster than 75.67% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
    # Memory Usage: 18.6 MB, less than 91.92% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ancestors_dict= self.get_ancestors_bfs(root, p, q)
        
        p_anc_dict= set()
        while p:
            # given all Node.val are unique, we just need to check node's value!
            p_anc_dict.add(p.val)
            p = ancestors_dict[p]
        
        while q:
            if q.val in p_anc_dict:
                return q
            q = ancestors_dict[q]
        
        
    def get_ancestors_bfs(self, root, target_node1, target_node2):
        
        parent_dict= dict()
        parent_dict[root] = None
        
        nodes_q= [root]
        while target_node1 not in parent_dict or target_node2 not in parent_dict:
            node= nodes_q.pop(0)
                            
            if node.left:
                parent_dict[node.left]= node
                nodes_q.append(node.left)
            if node.right:
                parent_dict[node.right]= node
                nodes_q.append(node.right)
            
        return parent_dict