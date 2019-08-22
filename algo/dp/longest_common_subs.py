class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # Maximum common substring
        m, n = len(A), len(B)
        if m == 0 or n == 0:
            return 0
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0):
                    dp[i][j] = A[i] == B[j]
                elif A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
        return int(max([max(row) for row in dp]))
