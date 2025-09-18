class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      dp = [False] * (len(s) + 1)
      dp[0] = True
      canMake = [0]
      for i in range(1,len(s)+1):
        for index in canMake:
          if s[index:i] in wordDict:
            dp[i] = True 
            canMake.append(i)
            break 
      return dp[-1]
        
          
        