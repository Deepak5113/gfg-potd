class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix):
        # code here
        n = len(matrix)
        m = len(matrix[0])
        left, right, top, down = 0, m-1, 0, n-1
        res = []
        while left <= right and top <= down:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, down+1):
                res.append(matrix[i][right])
            right -= 1
            if top <= down:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if left <= right:
                for i in range(down, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res


# {
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))

# } Driver Code Ends
