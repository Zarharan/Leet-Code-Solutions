# URL: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# 1249. Minimum Remove to Make Valid Parentheses

# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
 

# Constraints:

# 1 <= s.length <= 10**5
# s[i] is either'(' , ')', or lowercase English letter.


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack= []
        extra_chars_index = set()
        for idx, char in enumerate(s):
            if char== "(":
                stack.append(idx)
            elif char== ")":
                if len(stack)>0:
                    stack.pop()
                else:
                    extra_chars_index.add(idx)
        
        for idx in stack:
            extra_chars_index.add(idx)
        
        result=""
        for idx, char in enumerate(s):
            if idx in extra_chars_index:
                continue
            
            result+= char
            
        return result