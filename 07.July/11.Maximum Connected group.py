from typing import List


class Solution:
    def MaxConnection(self, grid: List[List[int]]) -> int:
        # code here
        n = len(grid)
        if n == 0:
            return 0

        # Directions for top, bottom, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Initialize the labels and sizes
        label = [[0] * n for _ in range(n)]
        sizes = []
        label_id = 0

        def dfs(x, y, label_id):
            stack = [(x, y)]
            label[x][y] = label_id
            size = 0

            while stack:
                cx, cy = stack.pop()
                size += 1

                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and label[nx][ny] == 0:
                        label[nx][ny] = label_id
                        stack.append((nx, ny))

            return size

        # Find all connected components and their sizes
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and label[i][j] == 0:
                    label_id += 1
                    size = dfs(i, j, label_id)
                    sizes.append(size)

        max_connected = max(sizes) if sizes else 0

        # Check each 0 cell to see the effect of changing it to 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    connected_size = 1  # this cell itself
                    seen_labels = set()

                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            label_id = label[ni][nj]
                            if label_id not in seen_labels:
                                connected_size += sizes[label_id - 1]
                                seen_labels.add(label_id)

                    max_connected = max(max_connected, connected_size)

        return max_connected


# {
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        grid = IntMatrix().Input(n, n)

        obj = Solution()
        res = obj.MaxConnection(grid)

        print(res)

# } Driver Code Ends
