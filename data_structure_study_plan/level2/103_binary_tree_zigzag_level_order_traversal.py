# URL: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# 103. Binary Tree Zigzag Level Order Traversal

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 
# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100


from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Runtime: 43 ms, faster than 72.75% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
    # Memory Usage: 14.1 MB, less than 57.55% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        result= defaultdict(list)
        level_q= [(root,0)]
        
        while level_q:
            target_node, level= level_q.pop(0)
            
            if level%2==0:
                result[level].append(target_node.val)
            else:
                result[level].insert(0,target_node.val)
            
            if target_node.left:
                level_q.append((target_node.left,level+1))
            if target_node.right:
                level_q.append((target_node.right,level+1))
        
        return result.values()
