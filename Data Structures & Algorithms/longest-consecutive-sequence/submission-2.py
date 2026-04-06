class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res_elem = []
        maxLength = 0
        temp_elem = []
        sorted_nums = list(set(nums))
        sorted_nums = sorted(sorted_nums)        
        if len(sorted_nums) == 0: return maxLength
        if len(sorted_nums) == 1: return 1
        print(sorted_nums)
        temp_elem.append(sorted_nums[0])
        for i in range(1,len(sorted_nums)):
            print(sorted_nums[i], i)
            if sorted_nums[i] == sorted_nums[i-1] + 1:
                temp_elem.append(sorted_nums[i])
                maxLength = max(len(temp_elem), maxLength)
                print(temp_elem)
            else:
                res_elem.append(temp_elem)
                maxLength = max(len(temp_elem), maxLength)
                temp_elem = []
                temp_elem.append(sorted_nums[i])
                print(res_elem, maxLength)
        return maxLength

