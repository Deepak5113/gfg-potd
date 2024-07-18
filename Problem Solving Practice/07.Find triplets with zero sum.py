# User function Template for python3

import sys
import io
import atexit


class Solution:
    # Function to find triplets with zero sum.
    def findTriplets(self, arr, n):
        # code here
        # Step 1: Sort the array
        arr.sort()

        # Step 2: Traverse the array and use two-pointer technique for each element
        for i in range(n - 2):
            # Left and right pointers
            left = i + 1
            right = n - 1

            while left < right:
                total = arr[i] + arr[left] + arr[right]

                # If sum is zero, return True
                if total == 0:
                    return True
                # If sum is less than zero, move the left pointer to the right
                elif total < 0:
                    left += 1
                # If sum is greater than zero, move the right pointer to the left
                else:
                    right -= 1

        # If no triplet found, return False
        return False


# {
 # Driver Code Starts
# Initial Template for Python 3
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        if (Solution().findTriplets(a, n)):
            print(1)
        else:
            print(0)

# } Driver Code Ends
