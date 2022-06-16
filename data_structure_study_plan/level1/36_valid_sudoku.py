from collections import defaultdict
import numpy as np


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        col=0
        row=0
        sub_box_idx=0
        
        board_arr = np.array(board)
        
        for i in range(1,10):
            # check row by row
            temp_row= board_arr[i-1:i]
            row_dict = defaultdict(int)
            for item in temp_row[0]:
                if row_dict[item]>0:
                    return False
                elif str(item)!= '.':
                    row_dict[item] +=1                        

            # check col by col
            temp_col = board_arr[:,i-1:i]
            col_dict = defaultdict(int)
            for item in temp_col[:,0]:
                if col_dict[item]>0:
                    return False
                elif str(item)!= '.':
                    col_dict[item] +=1
        
        while sub_box_idx<9:
            sub_box_dict = defaultdict(int)
            col = (sub_box_idx % 3)*3
            row = (sub_box_idx // 3)*3         
           
            sub_box = board_arr[row:row +3, col:col+3]
            # print(sub_box)            
                
            for item in sub_box.flatten():
                if sub_box_dict[item]>0:
                    return False
                elif str(item)!= '.':
                    sub_box_dict[item] +=1

            
            sub_box_idx +=1
        
        return True
            
            
        
        
            