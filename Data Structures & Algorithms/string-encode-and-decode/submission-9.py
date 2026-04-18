class Solution:


    def encode(self, strs: List[str]) -> str:
        x = ""
        for e in strs:
            x = x + str(len(e)) +"#" + e
        return x

    def decode(self, s: str) -> List[str]:
        x = list()
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i + length
            x.append(s[i:j])
            i = j 

        return x

        