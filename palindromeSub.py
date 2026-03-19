class Example:
    def palindromSub(self, s: str) -> int:
        # print('Hello World')
        # subs = []
        # palinDromeSet = set()
        # n  = len(s)
        # for i in range(n):
        #     for j in range(i+1 , n+1):
        #         if s[i:j] not in palinDromeSet and s[i:j][::-1] == s[i:j]:
        #             palinDromeSet.add(s[i:j])
        #             subs.append(s[i:j])
        #         elif s[i:j] in palinDromeSet:
        #             subs.append(s[i:j])
        #         else:
        #             continue
                    
            
        # return subs
        
        count = 0
        n = len(s)
        
        def check(lp , rp):
            nonlocal count
            while lp >= 0 and rp < n and s[lp] == s[rp]:
                count+=1
                lp-=1
                rp+=1
                
        for i in range(n):
            check(i,i)
            check(i,i+1)
            
        return count
        


    if __name__ == '__main__':
       solution = palindromSub('','abc')
       print(solution)
       
