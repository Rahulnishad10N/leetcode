class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n=len(graph)
        visited=[False for _ in range(n)]
        result=[]
        path=[]

        def allPath(graph,src,dest,visited,path,result):
            visited[src]=True
            path.append(src)
            if src==dest:
                result.append(path.copy())
            else:
                for neighbour in graph[src]:
                    if not visited[neighbour]:
                        allPath(graph,neighbour,dest,visited,path,result)

            path.pop()
            visited[src]=False

        allPath(graph,0,n-1,visited,path,result)
        return result    