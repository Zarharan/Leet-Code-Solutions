# URL: https://leetcode.com/problems/01-matrix/

# 542. 01 Matrix

# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

# Example 1:

# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:

# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
 
# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10**4
# 1 <= m * n <= 10**4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.


from collections import defaultdict

class Graph:
    def __init__(self, matrix):
        self.adjacents= defaultdict(list)
        self.distances= matrix[:][:]
        self.unmarked_vertex= set()
        self.vertexs= defaultdict(int)
        self.zeros= []
        
        adjacents_indexes= [[1,0],[0,1],[-1,0],[0,-1]]        
        for row_idx in range(len(matrix)):
            for col_idx in range(len(matrix[0])):
                vertex_key= self.get_key(row_idx, col_idx)                
                self.vertexs[vertex_key]= matrix[row_idx][col_idx]
                
                if matrix[row_idx][col_idx] == 0:
                    self.zeros.append(vertex_key)                    
                
                self.unmarked_vertex.add(vertex_key)
                for adj in adjacents_indexes:
                    if row_idx+adj[0] >= 0 and row_idx+adj[0]< len(matrix) and col_idx+adj[1] >= 0 and col_idx+adj[1]< len(matrix[0]):                       
                        
                        self.adjacents[vertex_key].append(self.get_key(row_idx+adj[0], col_idx+adj[1]))
                        if matrix[row_idx+adj[0]][col_idx+adj[1]] == 0:
                            self.distances[row_idx][col_idx]= 1
                    

    def get_key(self, row_idx, col_idx):
        return str(row_idx)+"#"+str(col_idx)
    
    
    def get_indexes_of_key(self, key):
        return [int(x) for x in key.split("#")]
    
    
    def get_value(self, vertex_key):
        return self.vertexs[vertex_key]
    
    def get_adjacents(self, vertex):
        return self.adjacents[vertex]
    
    
    def mark(self, vertex):
        if vertex in self.unmarked_vertex:
            self.unmarked_vertex.remove(vertex)
            
    
    def is_mark(self, vertex):
        return not vertex in self.unmarked_vertex
    
    
    def get_unmarked(self):
        if len(self.unmarked_vertex)>0:
            target_vertex= self.unmarked_vertex.pop()
            self.unmarked_vertex.add(target_vertex)
            return target_vertex
        
        return None
    
    
    def calc_distance_using_bfs(self):
        
        bfs_q=[]
        for zero_v in self.zeros:
            bfs_q.append((zero_v, 0))
        
        # BFS
        while bfs_q:
            target_v, distance= bfs_q.pop(0)

            if self.is_mark(target_v):
                continue

            self.mark(target_v)
            indexes= self.get_indexes_of_key(target_v)
            if self.get_value(target_v)== 0:
                self.distances[indexes[0]][indexes[1]]= 0
            else:
                self.distances[indexes[0]][indexes[1]]= distance

            adjacents= self.get_adjacents(target_v)            

            for adj in adjacents:
                bfs_q.append((adj, distance+1))
            
    
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        graph= Graph(mat)
        
        graph.calc_distance_using_bfs()
        
        return graph.distances