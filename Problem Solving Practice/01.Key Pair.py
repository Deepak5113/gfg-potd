# User function Template for python3
class Solution:
    def hasArrayTwoCandidates(self, arr, x):
        # code here
        seen = set()
        for num in arr:
            if x-num in seen:
                return True
            seen.add(num)
        return False


# {
 # Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.hasArrayTwoCandidates(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        # print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
