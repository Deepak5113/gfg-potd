# User function Template for python3
from collections import deque, defaultdict


class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Initialize the distance array with -1
        distance = [-1] * n
        distance[src] = 0

        # BFS setup
        queue = deque([src])

        while queue:
            node = queue.popleft()

            # Explore all neighbors
            for neighbor in adj[node]:
                if distance[neighbor] == -1:  # If not visited
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)

        return distance


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges = []
        for i in range(m):
            li = list(map(int, input().split()))
            edges.append(li)
        src = int(input())
        ob = Solution()
        ans = ob.shortestPath(edges, n, m, src)
        for i in ans:
            print(i, end=" ")
        print()
        tc -= 1
# } Driver Code Ends
