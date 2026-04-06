class Solution:
    def reverse(self, x: int) -> int:
        if x > 2147483647 or x < -2147483648 : return 0
        op = 0
        res = abs(x)
        # print(aX)
        arr = []
        # res, rem = divmod(aX, 10)
        # print(res, rem)
        while res:
            res, rem = divmod(res, 10)
            arr.append(rem)
            # print(res,rem, arr)
        for i in range(len(arr)):
            # print(i, arr[i], op * 10  + arr[i], op)
            op = (op * 10  + arr[i])
        if x < 0:
            op = op * -1
        
        if op > 2147483647 or op < -2147483648:
            return 0
        else:
            return op