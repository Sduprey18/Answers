class Solution:
    def fib(self, n: int) -> int:
      
      memo = {}
      def dp(n,memo):
        if n in memo:
          return memo[n]
        if n == 0:
          memo[n] = 0
          return memo[n]
        if n == 1:
          memo[n] = 1
          return memo[n]
        if n<=4:
          memo[n] = n-1
          return memo[n]
        memo[n] = dp(n-1, memo) + dp(n-2, memo)
        return memo[n]
      
      return dp(n,memo)
