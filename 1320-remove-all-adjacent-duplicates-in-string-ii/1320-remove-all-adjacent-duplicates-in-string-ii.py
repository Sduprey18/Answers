class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        #keep pairs of [letter, count]
        for letter in s:
            if stack:
                if stack[-1][0] == letter:
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop()
                else:
                    stack.append([letter,1])
            else:
                stack.append([letter,1])
        
        fullString = []
        for letter,count in stack:
            for i in range(count):
                fullString.append(letter)

        res = "".join(fullString)

        return res