class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # rotated_array = []
        # for i in range(target):
        #     rotated_array.append(nums.pop(1))
        #     nums = nums[:len(nums)-1]
        # rotated_array = rotated_array + nums
        return(target in nums)