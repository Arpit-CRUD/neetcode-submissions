class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        group=[1]*len(nums);
        prefix=1;
        for i in range(len(nums)):
            group[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            group[i]*=suffix
            suffix*=nums[i]
        return group