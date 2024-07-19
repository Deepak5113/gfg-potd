# User function Template for python3
class Solution:

    def constructLowerArray(self, arr):
        # code here
        def merge_sort(enum):
            half = len(enum) // 2
            if half:
                left, right = merge_sort(enum[:half]), merge_sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(arr)
        merge_sort(list(enumerate(arr)))
        return smaller


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
