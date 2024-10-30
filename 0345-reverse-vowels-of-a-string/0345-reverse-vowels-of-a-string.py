class Solution:
    def reverseVowels(self, s: str) -> str:
      vowels =['a','e','i','o','u', 'A','E','I','O','U']
      l = 0
      r = len(s) - 1
      print(s)
      arr = list(s)
      while l<r:
        if s[l] not in vowels:
          l+=1
          continue 
        if s[r] not in vowels:
          r-=1
          continue 
        arr[l], arr[r] = arr[r] , arr[l]
        l+=1
        r-=1
      res = ''.join(arr)
      return res
        