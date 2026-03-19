from collections import Counter


class Solution:
    def alternatingStr(self , s:str)-> int:
        str1= ''
        str2= ''
        c1 = 0
        c2 = 0
        for i in range(len(s)):
            if i%2 == 0:
                str1 += '0'
                str2 += '1'
            else:
                str1 += '1'
                str2 += '0'
        
        # print(str1 , str2)
        
        for i in range(len(s)):
            if s[i] != str1[i]:
                c1+=1
            if s[i] != str2[i]:
                c2+=1

        return min(c1 , c2)         
        
        
    
    
    


if __name__ == '__main__':
    sol = Solution()
    print(sol.alternatingStr("0100"))  #ans 1    :: 0 : 3  ---  1 : 1
    print(sol.alternatingStr("10"))    # ans 0   :: 0 : 1  ---  1 : 1 
    print(sol.alternatingStr("1111"))  # ans 2   :: 0 : 0  ---  1 : 4
    print(sol.alternatingStr("10010100"))  # ans 3 :0 : 5  ---  1 : 3
    
    #  IF FREQ IS EQUAL THEN 
    # ANS = FREQ 0 - FREQ 1 
    # 1010
    # ANS = 0 
    