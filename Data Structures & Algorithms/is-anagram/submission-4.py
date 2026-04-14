class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = dict()
        dict2 = dict()

        for e in s:
            if e in dict1:
                dict1[e] += 1
            else:
                dict1[e] = 1
        
        for e in t:
            if e in dict2:
                dict2[e] += 1
            else:
                dict2[e] = 1
        
        if dict1 == dict2:
            return True
        else:
            return False

        
        