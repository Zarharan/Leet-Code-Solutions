# Url: https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 10**4
# s consists of parentheses only '()[]{}'.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        open_chars = ["(", "{", "["]
        for char in s:
            if char in open_chars:
                stack.append(char)
                continue
            
            if len(stack) < 1:
                return False
            top_char = stack.pop()            
            if char == ")" and top_char != "(":
                return False
            
            if char == "}" and top_char != "{":
                return False
                
            if char == "]" and top_char != "[":
                return False
            
        if len(stack)>0:
            return False
        
        return True
                
        