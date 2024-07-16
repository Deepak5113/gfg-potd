# User function Template for python3
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self, arr, n):
        # code here

        # Approach 1: Using Kadane's Algorithm
        # 		n=len(arr)
        # 		if n==0: return -1
        # 		ans=arr[0]
        # 		max_prod,min_prod=arr[0],arr[0]
        # 		for i in range(1,n):
        # 		    choice1=min_prod*arr[i]
        # 		    choice2=max_prod*arr[i]
        # 		    max_prod=max(arr[i],max(choice1,choice2))
        # 		    min_prod=min(arr[i],min(choice1,choice2))
        # 		    ans=max(ans,max_prod)
        # 		return ans

        # Approach 2: Travesing from start and end of the array
        left_prod = 1
        right_prod = 1
        max_prod = arr[0]
        for i in range(len(arr)):
            if left_prod == 0:
                left_prod = 1
            if right_prod == 0:
                right_prod = 1
            left_prod *= arr[i]
            right_prod *= arr[len(arr)-1-i]
            max_prod = max(max_prod, max(left_prod, right_prod))
        return max_prod


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
