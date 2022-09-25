class Solution:
    def bin2dec(self, num):
        num = num[::-1]
        res = 0
        for i in range(len(num)):
            if num[i] == "1":
                res += 2**i
        return res
    
    def dec2bin(self, num):
        res = ""
        while num:
            if num%2 == 0:
                res = "0" + res
            else:
                res = "1" + res
            num //= 2
            
        if len(res) == 0:
            res = "0"
        return res
        
    def addBinary(self, a: str, b: str) -> str:
        calc = self.bin2dec(a) + self.bin2dec(b)
        # print(self.bin2dec(a), self.bin2dec(b))
        return self.dec2bin(calc)
        
