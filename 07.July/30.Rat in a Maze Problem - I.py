from typing import List


class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        # code here
        n = len(m)
        if m[0][0] == 0 or m[n-1][n-1] == 0:
            return []

        directions = {'D': (1, 0), 'L': (0, -1), 'R': (0, 1), 'U': (-1, 0)}
        result = []

        def dfs(x, y, path):
            if x == n - 1 and y == n - 1:
                result.append(path)
                return

            temp = m[x][y]
            m[x][y] = 0

            for direction, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and m[nx][ny] == 1:
                    dfs(nx, ny, path + direction)

            m[x][y] = temp

        dfs(0, 0, "")
        result.sort()
        return result


# {
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# } Driver Code Ends
