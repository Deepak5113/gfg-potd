# User function Template for python3

import math


class Solution:
    # Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        # Your code here
        max_sum = arr[0]
        curr_sum = 0
        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum > max_sum:
                max_sum = curr_sum

            if curr_sum < 0:
                curr_sum = 0
        return max_sum


# {
 # Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
