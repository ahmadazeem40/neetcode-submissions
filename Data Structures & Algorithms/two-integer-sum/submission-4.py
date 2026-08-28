class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        
        for index, num in enumerate(nums):
            comp = target - num
            if comp in x:
                return[x[comp], index]
            x[num] = index