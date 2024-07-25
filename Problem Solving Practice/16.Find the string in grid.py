# User function Template for python3

class Solution:
    def searchWord(self, grid, word):
        # Code here
        rows = len(grid)
        cols = len(grid[0])
        word_len = len(word)

        # 8 possible directions
        directions = [
            (0, 1),   # right
            (0, -1),  # left
            (1, 0),   # down
            (-1, 0),  # up
            (1, 1),   # down-right
            (1, -1),  # down-left
            (-1, 1),  # up-right
            (-1, -1)  # up-left
        ]

        # Helper function to check if the word can be found starting from (r, c) in direction (dr, dc)
        def check_direction(r, c, dr, dc):
            for k in range(word_len):
                nr, nc = r + dr * k, c + dc * k
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[k]:
                    return False
            return True

        result_set = set()

        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == word[0]:  # First character matches
                    for dr, dc in directions:
                        if check_direction(r, c, dr, dc):
                            result_set.add((r, c))

        # Convert the set to a sorted list
        result = sorted(list(result_set))
        return result


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        grid = []
        for _ in range(n):
            cur = input()
            temp = []
            for __ in cur:
                temp.append(__)
            grid.append(temp)
        word = input()
        obj = Solution()
        ans = obj.searchWord(grid, word)
        for _ in ans:
            for __ in _:
                print(__, end=" ")
            print()
        if len(ans) == 0:
            print(-1)

# } Driver Code Ends
