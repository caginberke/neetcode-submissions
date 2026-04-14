class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for e in nums:
            if e in mySet:
                return True
            mySet.add(e)
        return False