# URL: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# 297. Serialize and Deserialize Binary Tree

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Example 1:

# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:

# Input: root = []
# Output: []
 
# Constraints:

# The number of nodes in the tree is in the range [0, 10**4].
# -1000 <= Node.val <= 1000


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # Runtime: 136 ms, faster than 89.62% of Python3 online submissions for Serialize and Deserialize Binary Tree.
    # Memory Usage: 20.2 MB, less than 64.55% of Python3 online submissions for Serialize and Deserialize Binary Tree.
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
            
        nodes_lst= []
        nodes_q= [root]
        
        while nodes_q:
            node= nodes_q.pop(0)
            
            if node:
                nodes_lst.append(node.val)                       
                nodes_q.append(node.left)
                nodes_q.append(node.right)
            else:
                nodes_lst.append(node)
        
        # Remove all None at the end of list.
        if len(nodes_lst)> 0:
            last_item= nodes_lst.pop()
            while len(nodes_lst)> 0 and last_item == None:
                last_item= nodes_lst.pop()

            nodes_lst.append(last_item)
        
        return str(nodes_lst).replace("[", "").replace("]", "").replace(" ", "")

    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        nodes_lst= data.split(",")
        
        if len(nodes_lst) == 0:
            return None
        
        nodes_dict= dict()
        
        for index in range(len(nodes_lst)):
            nodes_dict[index] = None if nodes_lst[index]== "None" else TreeNode(int(nodes_lst[index]))
            
        next_root= 0
        for index in range(len(nodes_lst)):
            if not nodes_dict[index]:
                continue
                
            right_idx= (next_root+1)*2 -1
            left_idx= (next_root+1)*2
            if right_idx< len(nodes_lst):
                nodes_dict[index].left= nodes_dict[right_idx]
            if left_idx< len(nodes_lst):
                nodes_dict[index].right= nodes_dict[left_idx]
            
            next_root+= 1
            
            if next_root> len(nodes_lst) // 2:
                break
            
        return nodes_dict[0]
    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))