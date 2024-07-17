# User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        # code here
        if n == 0:
            return []
        prefix_prod = [1]*n
        suffix_prod = [1]*n
        for i in range(1, n):
            prefix_prod[i] = prefix_prod[i-1]*nums[i-1]
        for i in range(n-2, -1, -1):
            suffix_prod[i] = suffix_prod[i+1]*nums[i+1]
        p = [1]*n
        for i in range(n):
            p[i] = prefix_prod[i]*suffix_prod[i]
        return p


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr, n)
        print(*ans)
# } Driver Code Ends
