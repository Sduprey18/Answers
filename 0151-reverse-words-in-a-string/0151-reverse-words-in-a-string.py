class Solution:
    def reverseWords(self, s: str) -> str:
        string = s.split()
        l, r = 0 , len(string)-1
        string.reverse()
        print(string)
        res = ' '.join(string)
        return res
