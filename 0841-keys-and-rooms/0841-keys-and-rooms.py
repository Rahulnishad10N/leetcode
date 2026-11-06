class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n=len(rooms)

        def dfs(rooms,src,visited):
            visited[src]=True

            for neighbour in rooms[src]:
                if not visited[neighbour]:
                    dfs(rooms,neighbour,visited)

        visited=[False for _ in range(n)]
        dfs(rooms,0,visited)

        for i in range(n):
            if not visited[i]:
                return False

        return True                    
        