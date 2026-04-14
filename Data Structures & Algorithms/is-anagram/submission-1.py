class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        myDict = dict()
        
        for letter in s:
            if letter in myDict:
                myDict[letter] += 1
            else:
                myDict[letter] = 1

        for letter in t:
            if letter in myDict:
                myDict[letter] -= 1
            else:
                myDict[letter] = -1
        
        for count in myDict.values():
            if count != 0:
                return False
        
        return True
