# User function Template for python3
import sys
import io
import atexit
import bisect


class Solution:
    def binary_search(self, key, brr):
        low, high = 0, len(brr) - 1
        index = -1
        while low <= high:
            mid = (low + high) // 2
            if brr[mid] <= key:
                index = mid
                low = mid + 1
            else:
                high = mid - 1
        return index

     # Function to count number of pairs such that x^y is greater than y^x.
    def countPairs(self, arr, brr):
        # code here
        ans = 0
        one = two = three_four = 0

        # Sort brr for binary search
        brr.sort()

        # Count occurrences of 1, 2, 3, and 4 in brr
        for x in brr:
            if x == 1:
                one += 1
            elif x == 2:
                two += 1
            elif x in (3, 4):
                three_four += 1

        # Count valid pairs
        for x in arr:
            if x != 1:
                ans += one
                if x == 2:
                    ans -= three_four
                if x == 3:
                    ans += two

                # Use binary search to find how many elements in brr are greater than x
                index = self.binary_search(x, brr)
                ans += len(brr) - index - 1

        return ans


# {
 # Driver Code Starts
# Initial Template for Python 3

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
        # M, N = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countPairs(a, b))
        # code here

# } Driver Code Ends
