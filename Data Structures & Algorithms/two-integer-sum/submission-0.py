class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visit_index = {}
        for i, num in enumerate(nums):
            residual = target - num
            if residual in visit_index:
                return [visit_index[residual], i]
            visit_index[num]= i
