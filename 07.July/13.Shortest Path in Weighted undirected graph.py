# User function Template for python3
from collections import defaultdict
from collections import deque
from typing import List


class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        # code here
        parent = list(range(n))
        dist = [float('inf')] * n
        adj = [[] for _ in range(n)]

        for edge in edges:
            u, v, wt = edge[0] - 1, edge[1] - 1, edge[2]
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        dist[0] = 0
        q = deque([[0, 0]])  # [node_wt, node]

        while q:
            node_wt, node = q.popleft()

            for adjnode, wt in adj[node]:
                if dist[adjnode] > wt + node_wt:
                    dist[adjnode] = wt + node_wt
                    parent[adjnode] = node
                    q.append([dist[adjnode], adjnode])

        if dist[n - 1] == float('inf'):
            return [-1]

        path = []
        r = n - 1
        while r != 0 and r != parent[r]:
            path.append(r + 1)
            r = parent[r]
        path.append(1)
        path.reverse()

        ans = [dist[n - 1]]
        ans.extend(path)
        return ans


# {
 # Driver Code Starts


def check(n, path, edges):
    gp = [{} for i in range(n + 1)]
    for u, v, w in edges:
        if v in gp[u]:
            gp[u][v] = min(gp[u][v], w)
        else:
            gp[u][v] = w

        if u in gp[v]:
            gp[v][u] = min(gp[v][u], w)
        else:
            gp[v][u] = w

    s = 0
    for i in range(2, len(path)):
        if path[i] not in gp[path[i - 1]]:
            return False
        s += gp[path[i - 1]][path[i]]

    return s == path[0]


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        edges = []
        for i in range(m):
            a, b, w = map(int, input().split())
            edges.append([a, b, w])

        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        if res[0] == -1:
            print(-1)
        else:
            if check(n, res, edges):
                print(res[0])
            else:
                print(-2)

# } Driver Code Ends
