class Solution:
    def func(self, i, j, dp):
        if i == 0 and j == 0:
            return 1
        
        if i < 0 or j < 0:
            return 0
        
       
        if dp[i][j] != -1:
            return dp[i][j]
        
       
        up = self.func(i - 1, j, dp)
        left = self.func(i, j - 1, dp)
        
        dp[i][j] = up + left
        return dp[i][j]
    
    
    def uniquePaths(self, m, n):
        dp = [[-1 for j in range(n)] for i in range(m)]
    
        return self.func(m - 1, n - 1, dp)

if __name__ == "__main__":
    m = 3
    n = 2
    
    sol = Solution()
    
    print("Number of ways:", sol.uniquePaths(m, n))