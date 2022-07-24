# URL: https://leetcode.com/problems/spiral-matrix-ii/

# 59. Spiral Matrix II

# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n**2 in spiral order.

 

# Example 1:


# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:

# Input: n = 1
# Output: [[1]]
 

# Constraints:

# 1 <= n <= 20


import numpy as np
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        if n==1:
            return [[1]]
        
        result_array= np.zeros((n,n), dtype=int)
        
        row_end_idx= n-1
        col_end_idx= n-1
        row_start_idx= 0
        col_start_idx= 0
        
        
        for i in range(n):
            result_array[0][i]= i+1
            
        counter= n+1
        row_index=1
        col_index= n-1
        row_step= 1
        col_step= -1
        for i in range(n-1,0,-1):
            for j in range(i):
                result_array[row_index][col_index]= counter
                counter+=1
                row_index+= row_step

            row_step= -(row_step)
            row_index+= row_step
            col_index+= col_step
            
            for k in range(i):
                result_array[row_index][col_index]= counter
                counter+=1
                col_index+= col_step
                
            col_step= -(col_step)
            col_index+= col_step
            row_index+= row_step           
        
        return result_array
                
            
                
            