# User function Template for python3
class Solution:
    def kPangram(self, string, k):
        # code here
        arr = [0]*26
        count, op = 0, 0
        for i in range(len(string)):
            if string[i].isalpha():
                arr[ord(string[i])-ord('a')] += 1
                count += 1
        for i in range(len(arr)):
            if arr[i] == 0:
                op += 1
        return op <= k and count >= 26


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends
