
import math


class Solution:
    def trappingWater(self, arr, n):
        # Code here
        if n < 3:
            return 0

        # Initialize two pointers
        left = 0
        right = n - 1

        # Initialize variables to store the maximum heights
        left_max = 0
        right_max = 0

        # Initialize the variable to store the total water trapped
        water_trapped = 0

        # Traverse the array
        while left <= right:
            if arr[left] < arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    water_trapped += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    water_trapped += right_max - arr[right]
                right -= 1

        return water_trapped

# {
 # Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.trappingWater(arr, n))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
