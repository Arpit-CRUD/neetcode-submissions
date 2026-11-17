class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        group=[]
        for i in nums:
            if i in group:
                return True
            else:
                group.append(i)
        return False