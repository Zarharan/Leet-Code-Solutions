# URL: https://leetcode.com/problems/number-of-provinces/

# 547. Number of Provinces

# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 # Example 1:

# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 
# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]


from collections import defaultdict
class Graph:
    def __init__(self,matrix):
        self.vertexes = defaultdict(list)
        self.unvisited = set()
        
        for row_idx in range(len(matrix)):
            self.vertexes[row_idx] = []
            self.unvisited.add(row_idx)
            for col_idx in range(len(matrix)):
                if matrix[row_idx][col_idx] == 1 and row_idx != col_idx:
                    self.vertexes[row_idx].append(col_idx)
                    
        
    def get_adjacents(self,vertex):
        return self.vertexes[vertex]
    
    
    def marked(self,vertex):
        self.unvisited.remove(vertex)
        
        
    def is_mark(self,vertex):
        return (not vertex in self.unvisited)
    
    
    def get_unmark_vertexes(self):
        """
        This function marks an unvisited vertex and returns it.
        """
        
        if len(self.unvisited)>0:
            return self.unvisited.pop()
            
        return None
                

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph = Graph(isConnected)
        target_v = graph.get_unmark_vertexes()
        counter = 0
        while target_v != None:
            self.bfs(target_v, graph)
            counter+=1
            target_v = graph.get_unmark_vertexes()            
            
        return counter
    
        
    def bfs(self,vertex, graph):
        queue = graph.get_adjacents(vertex)
        
        while len(queue)>0:
            target_v = queue.pop(0)            
            if graph.is_mark(target_v):
                continue
            
            graph.marked(target_v)        
            queue.extend(graph.get_adjacents(target_v))
                    
    
