# User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        n1 = len(arr1)
        n2 = len(arr2)

        low1, low2 = 0, 0
        count = 0

        while low1 < n1 and low2 < n2:
            if arr1[low1] < arr2[low2]:
                count += 1
                if count == k:
                    return arr1[low1]
                low1 += 1
            else:
                count += 1
                if count == k:
                    return arr2[low2]
                low2 += 1

        while low1 < n1:
            count += 1
            if count == k:
                return arr1[low1]
            low1 += 1

        while low2 < n2:
            count += 1
            if count == k:
                return arr2[low2]
            low2 += 1

        return -1


# {
 # Driver Code Starts
# Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(k, a, b))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
