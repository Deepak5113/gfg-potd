# User function Template for python3

class Solution:
    def findMin(self, arr, n):
        # complete the function here
        low = 0
        high = n-1
        while low < high:
            mid = low+(high-low)//2
            if arr[mid] > arr[high]:
                low = mid+1
            elif arr[mid] < arr[high]:
                high = mid
            else:
                end -= 1
        return arr[low]


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends
