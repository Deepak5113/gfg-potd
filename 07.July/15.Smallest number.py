# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3
import math
import sys


class Solution:
    def smallestNumber(self, s, d):
        # code here
        if (9 * d) < s:
            return '-1'

        ans = ['0'] * d

        for i in range(d - 1, -1, -1):
            if s > 9:
                ans[i] = '9'
                s -= 9
            else:
                ans[i] = str(s)
                s = 0
                break

        # Ensure the first digit is not zero by making necessary adjustments
        if ans[0] == '0':
            ans[0] = '1'
            for i in range(1, d):
                if ans[i] != '0':
                    ans[i] = str(int(ans[i]) - 1)
                    break

        return ''.join(ans)


# {
 # Driver Code Starts.
# Position this line where user code will be pasted.
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    s = int(data[index])
    d = int(data[index + 1])
    index += 2
    ob = Solution()
    print(ob.smallestNumber(s, d))

# } Driver Code Ends
