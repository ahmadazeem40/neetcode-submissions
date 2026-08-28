class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        
        for index, num in enumerate(nums):
            indices[num] = index
        
        for index, num in enumerate(nums):
            comp = target - num
            if comp in indices and indices[comp] != index:
                return[index, indices[comp]]