# URL: https://leetcode.com/problems/sort-characters-by-frequency/

# 451. Sort Characters By Frequency

# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
 
# Constraints:

# 1 <= s.length <= 5 * 10**5
# s consists of uppercase and lowercase English letters and digits.


class Solution:
    # Runtime: 48 ms, faster than 90.57% of Python3 online submissions for Sort Characters By Frequency.
    # Memory Usage: 15.3 MB, less than 81.42% of Python3 online submissions for Sort Characters By Frequency.
    
    # Total time complexity= O(n + 62Log(62)) = O(n)
    def frequencySort(self, s: str) -> str:
        
        # Count each character. There are at most 62 characters (s consists of uppercase and lowercase English letters and digits). Time complexity= O(n)
        counter_dict= Counter(s)        
        
        result_str= ""
        
        # Time complexity of sort of 62 characters= O(62log(62)) = Constant time
        for key, val in sorted(counter_dict.items(), key=lambda x: x[1], reverse=True):
            result_str += key * val
        
        return result_str