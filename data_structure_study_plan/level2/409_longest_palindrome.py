# URL: https://leetcode.com/problems/longest-palindrome/

# 409. Longest Palindrome


# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.


class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        seen_char= set()
        
        counter= 0
        for char in s:
            if char in seen_char:
                seen_char.remove(char)
                counter += 2
            else:
                seen_char.add(char)
                
        
        if len(seen_char)>0:
            counter += 1
        
        return counter