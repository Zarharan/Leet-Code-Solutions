# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# 82. Remove Duplicates from Sorted List II

# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Example 1:

# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# Example 2:

# Input: head = [1,1,1,2,3]
# Output: [2,3]
 
# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    
        if head== None or head.next== None:
            return head
        
        new_head= None
        current_node= None
        
        while head:
            counter= 1
            while head.next != None and head.val == head.next.val:
                head= head.next
                counter+= 1
            
            if counter == 1:
                if new_head == None:
                    new_head= head
                if current_node== None:
                    current_node= head
                else:
                    current_node.next= head
                    current_node= current_node.next
                    
            head= head.next
            if current_node:
                current_node.next= None
                       
        return new_head