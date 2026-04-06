class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        prevStart = []
        start = 0
        prevStart.append(start)
        end = 1
        if len(s) == 1 : return 1
        while(end < len(s)):
            c = s[end]
            print(s[start:end], c, start, end)
            if c in s[start:end]:
                # print(s[start:end], c, start, end)
                length = end - start
                maxlength = max(length, maxlength)
                prevStart.append(start)
                start = s[start:end].index(c) + 1 + prevStart.pop(1)
            else:
                length = end - start + 1
                maxlength = max(length, maxlength)
            end +=1
        return maxlength