class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for e in nums:
            mySet.add(e)
        if len(mySet) == len(nums):
            return False
        else:
            return True