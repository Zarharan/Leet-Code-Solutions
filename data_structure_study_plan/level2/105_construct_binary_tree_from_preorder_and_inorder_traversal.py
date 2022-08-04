# URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Example 1:

# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1] 

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.


from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Runtime: 72 ms, faster than 91.85% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
    # Memory Usage: 18.7 MB, less than 93.35% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.root_index= 0
        self.inorder_index= defaultdict(int)
        self.preorder= preorder
        
        for idx, root_val in enumerate(inorder):
            self.inorder_index[root_val]= idx
        
        return self.build_tree_helper(0, len(inorder)-1)
    
        
    def build_tree_helper(self, left_bound, right_bound):
        
        if left_bound>right_bound:
            return None
        
        root_val= self.preorder[self.root_index]
        root= TreeNode(root_val)
        self.root_index+= 1
        
        root.left= self.build_tree_helper(left_bound, self.inorder_index[root_val]-1)
        root.right= self.build_tree_helper(self.inorder_index[root_val]+1, right_bound)
        
        return root