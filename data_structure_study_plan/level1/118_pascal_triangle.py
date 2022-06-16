class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        result.append([1])
        if numRows == 1:
            return result
        result.append([1,1])
        
        if numRows == 2:
            return result
        
        for i in range(2, numRows):
            temp = [1]
            for j in range(len(result[i-1])-1):
                temp.append(result[i-1][j] + result[i-1][j+1])
            temp.append(1)
            result.append(temp)
        return result
        
        