# User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        if not arr:
            return "-1"

        shortest_str = min(arr, key=len)

        for i in range(len(shortest_str)):
            for string in arr:
                if string[i] != shortest_str[i]:
                    return shortest_str[:i] if i > 0 else "-1"

        return shortest_str if shortest_str else "-1"


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends
