# Url: https://leetcode.com/problems/backspace-string-compare/

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
 

# Constraints:

# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
 

# Follow up: Can you solve it in O(n) time and O(1) space?


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return self.clean_text_with_stack(s) == self.clean_text_with_stack(t)
        # return self.clean_text_with_list(s) == self.clean_text_with_list(t)


    # First Solution
    def clean_text_with_stack(self, text):
        
        stack = []
        for char in text:
            if char =="#":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
    
    
    # Second Solution
    def clean_text_with_list(self, s):
        sharp_no = 0
        pointer = len(s)-1
        s_array = list(s)
        for char in s_array[::-1]:
            if char=="#":
                sharp_no +=1
            elif sharp_no>0:
                sharp_no -=1
            else:
                s_array[pointer] = char
                pointer -= 1
                
            # print(s_array)
        
        result = ''.join(s_array[pointer+1:])
        # print('-------- ',result)
        return result
               
                
                