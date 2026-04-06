class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =[]
        while len(strs):
            i = 0
            grp = []
            grp.append(strs[i])
            strMatch = strs[i]
            strs.remove(strs[i])
            for j in range(len(strs)):
                if sorted(strMatch) == sorted(strs[j]):
                    grp.append(strs[j])
            res.append(grp)
            for j in range(1, len(grp)):
                strs.remove(grp[j])
        return res
            
