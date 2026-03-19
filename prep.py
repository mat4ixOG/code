        
class Solution:
    def countSubstriings(self,s:str,c:str)->int :
        n = len(s)
        count = 0
        for i in range(n):
            for subs in range(i+1,n+1):
                if s[i] == c and s[subs-1] == c:
                    count+=1
                        
        return count         
                
    if __name__ == '__main__':
        res = countSubstriings('','abada','a')
        print(res)