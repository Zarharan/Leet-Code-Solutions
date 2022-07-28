# URL: https://leetcode.com/problems/multiply-strings/

# 43. Multiply Strings

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
 

# Constraints:

# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if len(num1)>len(num2):
            num2 = ("0"*(len(num1)- len(num2))) + num2
        else:
            num1 = ("0"*(len(num2)- len(num1))) + num1
            
        result= 0
        
        for idx, digit1 in enumerate(num1[::-1]):
            carry= 0
            middle_result= ""
            for digit2 in num2[::-1]:                
                digit_prodoct= int(digit1) * int(digit2) + carry
                middle_result = str(digit_prodoct % 10) + middle_result
                carry= digit_prodoct // 10
            
            middle_result= str(carry) + middle_result
            middle_result+= ("0"*idx)
            result += int(middle_result)
            
        return str(result)