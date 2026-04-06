class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        union = nums1 + nums2
        sortedFull = sorted(union)
        print(sortedFull)
        print(len(sortedFull)/2)
        # print(sortedFull[len(sortedFull)/2], sortedFull[len(sortedFull)/2])
        if len(sortedFull)%2 ==0:
            med = (sortedFull[int(len(sortedFull)/2)-1] + sortedFull[int(len(sortedFull)/2)])/2
        else:
            med = sortedFull[math.ceil(len(sortedFull)/2)-1]
        return med
