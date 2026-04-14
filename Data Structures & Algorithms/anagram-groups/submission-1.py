class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        combined = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1

            key = tuple(count)
            combined[key].append(word)
        
        return list(combined.values())


        