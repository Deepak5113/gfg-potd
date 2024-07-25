# User function Template for python3

class Solution:
    def factorial(self, N):
        # code here
        def calculate_factorial(N):
            result = 1
            for i in range(2, N+1):
                result *= i
            return result
        factorial_digits = calculate_factorial(N)
        return [int(digit) for digit in str(factorial_digits)]


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N)
        for i in ans:
            print(i, end="")
        print()

# } Driver Code Ends
