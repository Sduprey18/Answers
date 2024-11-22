class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #first we want to create indegree
        indegree = [0] * numCourses

        adjList = defaultdict(list)
        #making adj list
        
        for course, preReq in prerequisites:
            if preReq not in adjList:
                adjList[preReq] = []
            adjList[preReq].append(course)

            indegree[course] += 1
        
        q = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            #getting index for curr, to get nei
            index= q.pop(0)
            #getting list of nei
            curr = adjList[index]
            for child in curr:
                indegree[child] -=1
                if indegree[child] == 0:
                    q.append(child)
        
        total = sum(indegree)
        if total>0:
            return False
        return True



        