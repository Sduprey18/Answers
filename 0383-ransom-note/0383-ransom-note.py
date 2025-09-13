class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for letter in magazine:
            if letter not in counter:
                counter[letter] = 1
            else:
                counter[letter] += 1
        
        for letter in ransomNote:
            if letter in counter:
                counter[letter] -=1 
                if counter[letter] < 0:
                    return False
            else:
                return False

        return True
        
        