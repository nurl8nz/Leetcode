class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                summation = mul + res[i + j + 1]
                
                res[i + j + 1] = summation % 10
                res[i + j] += summation // 10
        
        while res and res[0] == 0:
            res.pop(0)
        
        return "".join(map(str, res))
