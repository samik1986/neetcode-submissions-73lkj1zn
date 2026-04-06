class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        res = []
        i = 0

        while i < len(s):
            cnt = i
            while s[cnt] != "#":
                cnt += 1
            length = int(s[i:cnt])
            i = cnt + 1
            cnt = i + length
            res.append(s[i:cnt])
            i = cnt
        return res

            
