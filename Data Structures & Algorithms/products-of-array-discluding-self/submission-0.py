class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # print(res)
        tot_prod = 1
        exists_zero = 0
        eps = 0.0001

        for n in nums:
            if n:
                tot_prod *= n
            else:
                exists_zero += 1

        print(tot_prod)
        for i in range(len(nums)):
            print(nums[i])
            if exists_zero>1:
                return [0] * len(nums)
            if exists_zero:
                if nums[i]:
                    res[i] = 0
                else:
                    res[i] = tot_prod
            else:
                res[i] = tot_prod // nums[i]

        return res