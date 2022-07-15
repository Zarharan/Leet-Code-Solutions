# URL: https://leetcode.com/problems/middle-of-the-linked-list/
# 876. Middle of the Linked List

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 
# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        # First solution (time complexity= O(n) and space complexity= O(n))
        def first_solution(head):
            nodes_lst=[]        
            while head != None:
                nodes_lst.append(head)
                head = head.next

            return nodes_lst[floor(len(nodes_lst) / 2)]
        
        
        # Second solution (time complexity= O(n) and space complexity= O(1))
        def second_solution(head):
            head_pointer= head
            tail_pointer= head
            
            while tail_pointer and tail_pointer.next:
                head_pointer= head_pointer.next
                tail_pointer= tail_pointer.next.next

            return head_pointer
            
        
        # return first_solution(head)
        return second_solution(head)