class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        left, right = 0, n - 1
        
        while left < right:
            if mat[left][right] == 1:
                left += 1
            else:
                right -= 1
        
        candidate = left

        for i in range(n):
            if i != candidate:
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1
        
        return candidate


#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))

# } Driver Code Ends