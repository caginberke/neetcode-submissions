class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for e in nums:
            if e in d:
                return True
            d[e] = 0
        return False
            
