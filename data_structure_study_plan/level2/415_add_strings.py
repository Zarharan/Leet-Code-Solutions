# URL: https://leetcode.com/problems/add-strings/

# 415. Add Strings

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"
 

# Constraints:

# 1 <= num1.length, num2.length <= 10**4
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        carry_in = 0
        total_steps= max(len(num1), len(num2))
        if len(num1)<total_steps:
            num1= ("0"*(total_steps-len(num1)))+num1
        else:
            num2= ("0"*(total_steps-len(num2)))+num2                  
        
        result= ""
        for idx in range(total_steps-1, -1,-1):
            digit1= num1[idx]
            digit2= num2[idx]
            
            total_sum= int(digit1) + int(digit2) + carry_in
            result= str(total_sum%10) + result
            carry_in= total_sum//10
                
        if carry_in>0:
            result= str(carry_in) + result
            
        return result