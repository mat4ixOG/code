class Solution:
    def dominoes(self, dominos:str)-> str:
        res= []
        n = len(dominos)
        states = [0] * n
        force = 0
        for i in range(n):
            if dominos[i] == "R":
                force = n
            elif dominos[i] == "L":
                force = 0
            else:
                force = max(force - 1, 0)
            states[i] += force
        force = 0
        for i in range(n-1 , -1 ,-1):
            if dominos[i] == "L":
                force = n
            elif dominos[i] == "R":
                force = 0
            else:
                force = max(force - 1, 0)
            states[i] -= force
        for i in states:
            if i > 0:
                res.append("R")
            elif i < 0:
                res.append("L")
            else:
                res.append(".")
        res = "".join(res)
        print(res)
        
        
if __name__ == "__main__":
    s = Solution()
    s.dominoes("..R..L..")
    
    s.dominoes(".L..R...L") 
    s.dominoes(".L.R...LR..")