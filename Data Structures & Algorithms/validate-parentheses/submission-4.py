class Solution:
    def isValid(self, s: str) -> bool:
        sParen = ['[', '(', '{']
        eParen = [']', ')', '}']
        paren = [('[',']'), ('(',')'), ('{','}')]
        hP = dict(paren)
        sT = []
        if len(s) % 2 != 0 : return False
        r = 0
        # l,r = len(s)//2-1, len(s)//2
        while r < len(s):
            print(r, s[r])
            if s[r] in sParen: 
                sT.append(s[r]) 
                print(sT)
            else: 
                if len(sT) > 0:
                    cS = sT.pop()
                    print(r, s[r], cS)
                    if cS == None: return False
                    if hP[cS] != s[r]: return False
                else:
                    return False
            r += 1
        return len(sT) == 0