# URL: https://leetcode.com/problems/surrounded-regions/

# 130. Surrounded Regions

# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

# Example 1:


# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
# Example 2:

# Input: board = [["X"]]
# Output: [["X"]]
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.


from collections import defaultdict

class Graph:
    def __init__(self, matrix):
        self.vertexs = dict()
        self.adjacents = defaultdict(list)
        self.unvisited = set()
        self.previous_node = dict()
        self.border_os = set()
        neighbor_idx = [[-1,0], [1,0], [0,-1], [0,1]]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                hash_key= self.get_vertex_hash_key(i,j)
                self.vertexs[hash_key] = matrix[i][j]
                if matrix[i][j]=="O":
                    self.unvisited.add(hash_key)
                    
                    if i == 0 or j == 0 or i == (len(matrix) - 1) or j == (len(matrix[0]) - 1):
                        self.border_os.add(hash_key)
                    
                    for n_idx in neighbor_idx:
                        if i+n_idx[0]<len(matrix) and i+n_idx[0]>=0 and j+n_idx[1]<len(matrix[0]) and j+n_idx[1]>=0 and matrix[i+n_idx[0]][j+n_idx[1]] == "O":
                            self.adjacents[hash_key].append(self.get_vertex_hash_key(i+n_idx[0],j+n_idx[1]))
        
        
    def get_vertex_hash_key(self, i,j):
        return str(i) + "," + str(j)
    
    
    def get_hash_key_indexs(self, hash_key):
        return [int(s) for s in hash_key.split(',')]
        
        
    def get_vertex(self, i,j):
        return self.vertexs[self.get_vertex_hash_key(i,j)]
    
    def get_adjacents(self, vertex):
        return self.adjacents[vertex]
    
    
    def mark(self, vertex):
        if vertex in self.unvisited:
            self.unvisited.remove(vertex)
            
            
    def is_mark(self, vertex):
        return not vertex in self.unvisited
        
        
    def get_unvisited_vertex(self):
        if len(self.unvisited)>0:
            return self.unvisited.pop()
        
        return None
    
    
    def get_border_os(self):
        return list(self.border_os)
    

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if  len(board) == 1 or len(board[0])==1:
            return
        
        graph = Graph(board)        
        # bfs only for border O's
        bfs_q= graph.get_border_os()
        while bfs_q:
            target_v = bfs_q.pop(0)
            if graph.is_mark(target_v):
                continue
            graph.mark(target_v)
            adjacents= graph.get_adjacents(target_v)
            bfs_q.extend(adjacents)
        
        # Change all unvisited O's to X
        unvisited_v = graph.get_unvisited_vertex()
        while unvisited_v:
            target_idx= graph.get_hash_key_indexs(unvisited_v)
            board[target_idx[0]][target_idx[1]]= "X"
            unvisited_v = graph.get_unvisited_vertex()
               
        return