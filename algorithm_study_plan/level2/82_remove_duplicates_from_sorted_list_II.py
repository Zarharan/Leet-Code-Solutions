# Url: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

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
        if head == None:
            return None
        
        if head.next == None:
            return head
        
        out_of_range = -1000
        last_node = ListNode(out_of_range, None)
        front = None
        next_item = head.next
        current = head
        pre_node = ListNode(out_of_range, None)
        
        while current != None:
            next_val = out_of_range
            if next_item != None:
                next_val = next_item.val
            if next_val != current.val and pre_node.val != current.val:
                if front == None:
                    last_node = current
                    front = last_node                    
                else:
                    last_node.next = current
                    last_node= last_node.next
                
            pre_node = current
            if next_item != None:
                next_item = next_item.next
            current = current.next
        
        last_node.next = None
        return front
        