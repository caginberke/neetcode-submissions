class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for e in nums:
            if e in d:
                return True
            d.add(e)
        return False
            
