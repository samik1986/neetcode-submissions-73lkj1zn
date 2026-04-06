class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unf = {}

        maxF, l, res = 0, 0, 0
    
        for c in range(len(s)):
            unf[s[c]] = unf.get(s[c], 0) + 1
            maxF = max(maxF, unf[s[c]])

            while (c - l + 1) - maxF > k:
                unf[s[l]] -= 1
                l += 1
            res = max(res, c-l+1)
        return res
