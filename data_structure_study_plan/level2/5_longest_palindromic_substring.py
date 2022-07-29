# URL: https://leetcode.com/problems/longest-palindromic-substring/

# 5. Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 
# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s)<=1:
            return s
        
        self.start_pos= 0
        self.end_pos= 0                   
        
        for idx in range(len(s)):            
            # Current char may not be the center char
            self.get_around_center(s, idx, idx+1)
            
            # Current char may be the center char
            self.get_around_center(s, idx, idx)
                            
        return s[self.start_pos:self.end_pos+ 1]
        
    
    def get_around_center(self, s, left, right):

        while left>= 0 and right< len(s) and s[left]==s[right]:
            right+= 1
            left-= 1            

        if (right - left-1) > (self.end_pos-self.start_pos):
            self.start_pos, self.end_pos= left+1, right-1
