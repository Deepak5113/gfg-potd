# User function Template for python3


class Solution:

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickselect(self, arr, low, high, k):
        if low <= high:
            pi = self.partition(arr, low, high)

            if pi == k:
                return arr[pi]
            elif pi > k:
                return self.quickselect(arr, low, pi - 1, k)
            else:
                return self.quickselect(arr, pi + 1, high, k)
        return None

    def kthSmallest(self, arr, k):
        return self.quickselect(arr, 0, len(arr) - 1, k - 1)


# {
 # Driver Code Starts
# Initial Template for Python 3
# contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))

# } Driver Code Ends
