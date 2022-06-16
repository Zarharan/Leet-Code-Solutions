class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        if len(mat[0])*len(mat) != r*c:
            return mat
        
        if len(mat) == r and len(mat[0])==c:
            return mat
        
        result = []
        c_mat = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                c_mat.append(mat[i][j])
                
        for index in range(0,len(c_mat),c):
            result.append(c_mat[index:index+c])
            
        return result
            
            
            
            