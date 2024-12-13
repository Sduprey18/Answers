class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        #lets make adj list first
        adjList ={}
        for l, r in edges:
            if l not in adjList:
                adjList[l] = []
            if r not in adjList:
                adjList[r] = []
            adjList[l].append(r)
            adjList[r].append(l)

        #go thru adjList, take score with the highest in the adjList
        scores =[0] * (len(edges)+1)
        print(len(edges)+1)
        for key,value in adjList.items():
            for thing in value:
                print(thing)
                scores[thing-1] +=1
        
        _max = max(scores)
        return (scores.index(_max)) + 1

            

        
     
        