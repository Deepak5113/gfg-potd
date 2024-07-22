# User function Template for python3

class Solution:

    def findMinDiff(self, A, N, M):

        # code here
        if N == 0 or M == 0:
            return 0
        A.sort()
        if N < M:
            return False
        min_diff = A[N-1]-A[0]
        i = 0
        for i in range(0, N-M+1):
            diff = A[i+M-1]-A[i]
            if diff < min_diff:
                min_diff = diff

        return min_diff


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())

        solObj = Solution()

        print(solObj.findMinDiff(A, N, M))
# } Driver Code Ends
