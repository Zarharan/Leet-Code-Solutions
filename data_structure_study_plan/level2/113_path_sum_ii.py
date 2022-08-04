# URL: https://leetcode.com/problems/path-sum-ii/

# 113. Path Sum II

# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

# Example 1:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
# Example 2:

# Input: root = [1,2,3], targetSum = 5
# Output: []
# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: []
 
# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Runtime: 73 ms, faster than 46.82% of Python3 online submissions for Path Sum II.
    # Memory Usage: 15.2 MB, less than 94.89% of Python3 online submissions for Path Sum II.m II.
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return []
        
        result= []
        node_stack= [(root, 0, [])]
        
        while node_stack:
            node, nodes_sum, val_lst= node_stack.pop()
            nodes_sum+= node.val
            val_lst.append(node.val)
            if not node.right and not node.left and targetSum== nodes_sum:
                result.append(val_lst)
            
            if node.right:
                node_stack.append((node.right, nodes_sum, val_lst.copy()))
            if node.left:
                node_stack.append((node.left, nodes_sum, val_lst.copy()))
        
        return result