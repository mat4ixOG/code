class Solution: 
   def minFlips(s: str) -> int:
    n = len(s)
    s = s + s
    
    alt1 = "".join("01"[i % 2] for i in range(2 * n))  
    alt2 = "".join("10"[i % 2] for i in range(2 * n))  

    res = float('inf')


    diff1 = sum(s[i] != alt1[i] for i in range(n)) 
    diff2 = sum(s[i] != alt2[i] for i in range(n))

    res = min(res, diff1, diff2)


    for i in range(n, 2 * n):
        if s[i] != alt1[i]:         diff1 += 1
        if s[i] != alt2[i]:         diff2 += 1
        
        left = i - n
        if s[left] != alt1[left]:   diff1 -= 1
        if s[left] != alt2[left]:   diff2 -= 1

        res = min(res, diff1, diff2)

    return res