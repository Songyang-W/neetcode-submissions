class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree= [0 for i in range(numCourses)]
        adj=[[] for i in range(numCourses)]
        for h,l in prerequisites:
            indegree[h]+=1
            adj[l].append(h)
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        finished_class=0
        while q:
            l=q.popleft()
            finished_class+=1
            for high_level_class in adj[l]:
                indegree[high_level_class]-=1
                if indegree[high_level_class]==0:
                    q.append(high_level_class)
        return finished_class==numCourses

            