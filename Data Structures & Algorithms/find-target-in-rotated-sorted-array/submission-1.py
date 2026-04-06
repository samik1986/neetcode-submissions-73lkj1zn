class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l,r = 0, len(nums)-1
        while l<r:
            # if nums[l] == target: return l+1
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid

        anchor = l

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] == target: return middle
                elif nums[middle] < target: left = middle + 1
                else: right = middle - 1
            return -1
        
        result = binary_search(0, anchor -1)
        if result != -1:
            return result
        
        return binary_search(anchor, len(nums)-1)