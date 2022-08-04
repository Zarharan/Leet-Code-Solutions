# URL: https://leetcode.com/problems/binary-tree-right-side-view/

# 199. Binary Tree Right Side View

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example 1:

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []
 
# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Runtime: 53 ms, faster than 48.28% of Python3 online submissions for Binary Tree Right Side View.
    # Memory Usage: 13.7 MB, less than 98.06% of Python3 online submissions for Binary Tree Right Side View.
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return None
        
        level_q= [(root, 0)]
        level_right_nodes= defaultdict(int)
        
        while level_q:
            node, level= level_q.pop(0)
            level_right_nodes[level]= node.val
            if node.left:
                level_q.append((node.left, level+1))
            if node.right:
                level_q.append((node.right, level+1))
            
        return level_right_nodes.values()