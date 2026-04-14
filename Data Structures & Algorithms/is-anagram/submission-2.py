class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = dict()
        t_dict = dict()

        for e in s:
            if e in s_dict:
                s_dict[e] = s_dict[e] + 1
            else:
                s_dict[e] = 0

        for j in t:
            if j in t_dict:
                t_dict[j] = t_dict[j] +1
            else:
                t_dict[j] = 0

        if s_dict == t_dict:
            return True
        else:
            return False