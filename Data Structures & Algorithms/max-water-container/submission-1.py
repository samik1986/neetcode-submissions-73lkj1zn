class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        idxB = 0
        idxE = len(heights)-1
        while(idxB<idxE):
            area = min(heights[idxB], heights[idxE]) * (idxE - idxB)
            res = max(res, area)
            if heights[idxB] <= heights[idxE]: 
                idxB += 1
            else: 
                idxE -= 1
        return res