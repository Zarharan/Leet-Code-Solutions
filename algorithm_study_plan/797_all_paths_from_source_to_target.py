# URL: https://leetcode.com/problems/all-paths-from-source-to-target/

# 797. All Paths From Source to Target

# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

# Example 1:


# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# Example 2:


# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
 

# Constraints:

# n == graph.length
# 2 <= n <= 15
# 0 <= graph[i][j] < n
# graph[i][j] != i (i.e., there will be no self-loops).
# All the elements of graph[i] are unique.
# The input graph is guaranteed to be a DAG.

from collections import defaultdict

class Graph:
    def __init__(self, matrix):
        self.vertexs = defaultdict(list)
        self.unvisited = set()
        self.parents = defaultdict(list)
        
        for i in range(len(matrix)):
            self.vertexs[i].extend(matrix[i])
            self.unvisited.add(i)
        
           
    def get_adjacents(self, vertex):
        return self.vertexs[vertex]
    

class Solution:
    def allPathsSourceTarget(self, graph_lst: List[List[int]]) -> List[List[int]]:
        bfs_q = [(0, [])]
        graph = Graph(graph_lst)
        destination = len(graph_lst)-1
        all_path= []
        
        while bfs_q:
            target_item= bfs_q.pop(0)
            target_v = target_item[0]
            adjacents= graph.get_adjacents(target_v)
            for adj in adjacents:
                bfs_q.append((adj, target_item[1] + [target_v]))
            
            if destination == target_v and target_item[1][0] == 0:
                all_path.append(target_item[1] + [target_v])
            
        return all_path