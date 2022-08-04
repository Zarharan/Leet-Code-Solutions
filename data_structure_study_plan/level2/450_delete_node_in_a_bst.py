# URL: https://leetcode.com/problems/delete-node-in-a-bst/

# 450. Delete Node in a BST

# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
 
# Example 1:

# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:

# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
# Example 3:

# Input: root = [], key = 0
# Output: []
 
# Constraints:

# The number of nodes in the tree is in the range [0, 10**4].
# -10**5 <= Node.val <= 10**5
# Each node has a unique value.
# root is a valid binary search tree.
# -10**5 <= key <= 10**5
 
# Follow up: Could you solve it with time complexity O(height of tree)?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Runtime: 86 ms, faster than 83.44% of Python3 online submissions for Delete Node in a BST.
    # Memory Usage: 18.4 MB, less than 77.49% of Python3 online submissions for Delete Node in a BST.
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return root
        
        target_node, pre_parent= self.find_node(root, key)
        if not target_node:
            return root
        
        new_child= None
        if target_node.right and target_node.left:
            inorder_successor_node= self.find_inorder_successor(target_node, key)
            inorder_successor_node.left= target_node.left
            inorder_successor_node.right= target_node.right            
            new_child= inorder_successor_node
                
        elif target_node.left:
            new_child= target_node.left
        elif target_node.right:
            new_child= target_node.right            
            
        #  When the target node to remove is root of the tree
        if not pre_parent:
            return new_child
        
        if pre_parent.left == target_node:
            pre_parent.left= new_child
        else:
            pre_parent.right= new_child
        
        return root
    
    
    def find_inorder_successor(self, root, val):
        inorder_successor_parent= root        
        inorder_successor_node= root.right
        while inorder_successor_node.left:
            inorder_successor_parent= inorder_successor_node
            inorder_successor_node= inorder_successor_node.left
            
        if inorder_successor_parent.left== inorder_successor_node:
            inorder_successor_parent.left= inorder_successor_node.right
        else:
            inorder_successor_parent.right= inorder_successor_node.right
            
        return inorder_successor_node
    
    
    def find_node(self, root, val):
        pre_parent= None
        while root:
            if root.val==val:
                return root, pre_parent
            
            pre_parent= root
            if root.val> val:
                root= root.left
            else:
                root= root.right
                
        return None, None