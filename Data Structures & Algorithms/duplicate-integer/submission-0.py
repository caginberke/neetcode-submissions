class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset=set();

        for element in nums:
            if element in myset:
                return True
            else:
                myset.add(element)
        return False