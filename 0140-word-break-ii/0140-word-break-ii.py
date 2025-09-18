class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res, sol = [] , []

        def backtrack(i):
            if i == len(s):
                sol.append((" ".join(res)))
                return 
            for j in range(i,len(s)):               
                if s[i:j+1] in wordDict:
                    res.append(s[i:j+1])
                    backtrack(j+1)
                    res.pop()
            return
        
        backtrack(0)
        return sol
        