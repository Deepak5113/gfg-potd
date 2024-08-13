# User function Template for python3


# Complete this function
import math


class Solution:
    def floorSqrt(self, n):
        # Your code here
        if n == 0 or n == 1:
            return n

        low, high = 0, n

        while low <= high:
            mid = (low + high) // 2
            if mid * mid == n:
                return mid
            elif mid * mid < n:
                low = mid + 1
                ans = mid
            else:
                high = mid - 1

        return ans


# {
 # Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):

        x = int(input())

        print(Solution().floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
