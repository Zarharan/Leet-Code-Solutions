# URL: https://leetcode.com/problems/search-a-2d-matrix-ii/

# 240. Search a 2D Matrix II

# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
 

# Example 1:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
# Example 2:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10**9 <= matrix[i][j] <= 10**9
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -10**9 <= target <= 10**9


class Solution:
    # First solution
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
                
        def binary_search(target_matrix):
            
            low= 0
            high= len(target_matrix)-1            
            
            while low<=high:
                mid = (low+high)//2            
                if target_matrix[mid]== target:
                    return mid
                
                if target>target_matrix[mid]:
                    low= mid+1
                else:
                    high= mid-1
            
            return -1
        
        row_index= 0
        target_row= matrix[row_index]
        while target_row[0] <= target:
            if target<=target_row[-1]:                 
                if binary_search(target_row[:])>=0:
                    return True
            row_index+=1
            if row_index< len(matrix):
                target_row= matrix[row_index]
            else:
                break
            
        return False


    # Second solution
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:                
        low= 0
        high= len(matrix[0])-1
        
        while (low<len(matrix) and high>=0):
            if matrix[low][high]== target:
                return True
            elif matrix[low][high]< target:
                low+=1
            else:
                high-= 1
            
        return False