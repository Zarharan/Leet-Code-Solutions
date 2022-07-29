# URL: https://leetcode.com/problems/add-two-numbers/

# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 
# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # First Solution
    # Runtime=117 ms, and Memory=14 MB
    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        first_num= ""
        while l1:
            first_num= str(l1.val) + first_num
            l1= l1.next
            
        second_num= ""
        while l2:
            second_num= str(l2.val) + second_num
            l2= l2.next
            
        total_sum = int(first_num) + int(second_num)
        
        pre_node= None
        for digit in str(total_sum):
            cur_node= ListNode(digit, pre_node)
            pre_node= cur_node
            
        return pre_node


    # Second Solution
    # Runtime=122 ms, and Memory=14 MB
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry_in= 0
        head= l1
        l1_last_node = head
        while l1 and l2:
            total_sum = carry_in + l1.val + l2.val
            carry_in= total_sum // 10
            l1.val= total_sum % 10
            l1_last_node= l1
            l1= l1.next
            l2= l2.next
                           
        if l2:
            l1_last_node.next = l2
        
        l1= l1_last_node.next
        
        while l1:
            total_sum = carry_in + l1.val
            carry_in= total_sum // 10               
            l1.val= total_sum % 10
            l1_last_node =l1
            l1= l1.next            
            
            if carry_in ==0:
                break
        
        if carry_in>0:
            l1_last_node.next= ListNode(carry_in)
        
        
        return head