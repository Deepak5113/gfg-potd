# User function Template for python3

class Solution:
    def search(self, arr, key):
        # Complete this function
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == key:
                return mid

            if arr[low] == arr[mid]:  # handles duplicates or when low and mid are at the same point
                low += 1

            elif arr[low] <= arr[mid]:  # if left half is sorted
                # checking if present in left sorted part
                if key >= arr[low] and key < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:  # if right half is sorted arr[low] > arr[mid]
                # checking if present in right half
                if key > arr[mid] and key <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))

# } Driver Code Ends
