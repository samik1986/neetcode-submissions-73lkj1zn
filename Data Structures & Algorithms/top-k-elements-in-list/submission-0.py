class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        elems = []
        counts = []
        nearest = 0
        for i in range(len(nums)):
            elem = nums[i]
            if elem not in elems:
                elems.append(elem)
                counts.append(1)
            else:
                counts[elems.index(elem)] += 1
                print(elems, counts)
        if len(elems) <= k:
            res = res + sorted(elems)
            return sorted(res)
        while nearest<k:
            maxCount = max(counts)
            res.append(elems[counts.index(maxCount)])
            elems.remove(elems[counts.index(maxCount)])
            counts.remove(maxCount)
            nearest += 1
        return sorted(res)
