
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        reverseAdjList = {i: [] for i in range(n)}

        # reverse the graph and create the indegree
        for i, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reverseAdjList[neighbor].append(i)
                indegree[i] += 1

        # add all 0's to q 
        q = []
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        res = []
        while q:
            curr = q.pop(0)
            res.append(curr)
            for neighbor in reverseAdjList[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return sorted(res)


                    
