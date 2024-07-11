# User function Template for python3

# arr    : list of integers denoting the elements of the array
# target : as specified in the problem statement

class Solution:
    def threeSumClosest(self, arr, target):
        # Your Code Here
        diff = float('inf')
        ans = 0

        # Sort the array
        arr.sort()

        # Iterate through the array
        for i in range(len(arr) - 2):
            j = i + 1
            k = len(arr) - 1

            while j < k:
                # Calculate the sum of the current triplet
                sum_val = arr[i] + arr[j] + arr[k]
                d = abs(sum_val - target)

                # If the current difference is smaller, update diff and ans
                if d < diff:
                    diff = d
                    ans = sum_val
                elif d == diff:
                    ans = max(ans, sum_val)

                # Move the pointers based on the comparison with the target
                if sum_val < target:
                    j += 1
                elif sum_val == target:
                    return sum_val
                else:
                    k -= 1

        return ans

# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.threeSumClosest(A, k))

# } Driver Code Ends
