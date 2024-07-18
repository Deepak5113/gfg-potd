# User function Template for python3
class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
       # code here
        n = len(arr)
        if n < 2:
            return n
        cb, bc = 1, 1
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                cb = 1+bc
            elif arr[i] < arr[i-1]:
                bc = 1+cb
        return max(cb, bc)


# {
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    tc = int(data[0])
    for i in range(1, tc + 1):
        s = data[i].strip().split()
        nums = list(map(int, s))
        obj = Solution()
        ans = obj.alternatingMaxLength(nums)
        print(ans)

# } Driver Code Ends
