# URL: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.level_dict = defaultdict(list)
        self.traversal(root, 0)
        
        for k,v in self.level_dict.items():
            print(k,v)
            
        return self.level_dict.values()
    
    
    def traversal(self, node, level):
        if not node:
            return
        
        self.level_dict[level].append(node.val)        
        self.traversal(node.left, level +1)
        self.traversal(node.right, level +1)
        