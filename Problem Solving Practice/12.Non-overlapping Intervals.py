# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3

class Solution:
    def minRemoval(self, N, intervals):
        # Code here
        if N <= 1:
            return 0

        # Sort intervals by their end time
        intervals.sort(key=lambda x: x[1])

        # Initialize the end of the last selected interval
        end = intervals[0][1]
        removal_count = 0

        # Iterate through intervals
        for i in range(1, N):
            if intervals[i][0] < end:
                # If the current interval starts before the end of the last selected interval,
                # it means they overlap and we need to remove one interval
                removal_count += 1
            else:
                # Otherwise, update the end to the end of the current interval
                end = intervals[i][1]

        return removal_count


# {
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(N, intervals)
        print(res)
# } Driver Code Ends
