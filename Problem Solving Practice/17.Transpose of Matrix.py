# User function Template for python3

class Solution:
    def transpose(self, matrix, n):
        # Approach for transpose of a square matrix

        for i in range(0, len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        return matrix

        # Approach for transpose of a matrix with different length of rows and columns

        # arr = [[0] * n for _ in range(n)]

        # # Fill the new matrix with transposed values
        # for i in range(n):
        #     for j in range(n):
        #         arr[j][i] = matrix[i][j]

        # # Update the original matrix with transposed values
        # for i in range(n):
        #     for j in range(n):
        #         matrix[j][i] = arr[j][i]
        # return matrix


# {
 # Driver Code Starts
# Initial Template for Python 3
for _ in range(int(input())):
    n = int(input())
    matrix = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    ob = Solution()
    ob.transpose(matrix, n)

    for row in matrix:
        print(*row)

# } Driver Code Ends
