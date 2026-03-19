class Example:
    def longestPalinSub(self, s: str) -> int:
        max_len = 0
        start = 0
        n = len(s)
        
        def check(lp , rp):
            while lp >= 0 and rp < n and s[lp] == s[rp]:
                lp-=1
                rp+=1
            return lp+1 , rp-1
                
        for i in range(n):
            # odd
            l1,r1 = check(i,i)
            if r1-l1 + 1 > max_len:
                start = l1
                max_len = r1 - l1 + 1
            # even
            l2 , r2 = check(i,i+1)
            if r2-l2 + 1 > max_len:
                start = l2
                max_len = r2 - l2 + 1
            
            
        return s[start: start + max_len]
        


    if __name__ == '__main__':
       solution = longestPalinSub('','babad')
       print(solution)