class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        n = len(edges)
        degree = [0] * (n + 2)

        for i, j in edges:
            degree[i] += 1
            degree[j] += 1

        for i in range(1, n + 2):
            if degree[i] == n:
                return i