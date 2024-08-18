class Solution:
    def canSplit(self, arr):
        # code here
        total_sum = sum(arr)
        curr_sum = 0
        for i in range(len(arr)-1):
            curr_sum += arr[i]
            if curr_sum*2 == total_sum:
                return True
        return False


# {
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends
