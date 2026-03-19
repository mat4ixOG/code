class Example:
    def minWindow(self, s: str, t: str) -> str:
        res = 0
        print('s:', s)
        l ,r = 0, len(s)
        print('l:', l , 'r:', r)
        while l<r: 
            if s[l] not in t:
                l += 1
            elif s[r-1] not in t:
                r -= 1
        print('l:', s[l] , 'r:', s[r])
        l += 1
           
            
                


    if __name__ == '__main__':
       solution = minWindow('','OUZODYXAZV' , 'XYZ')
       print(solution)