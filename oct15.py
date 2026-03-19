class Example:
    def example(self, s: str) -> int:
        minSteps = 0
        for i in range(len(s)):
            for j in range(len(s)-i):
                if s[j] != s[j+i]:
                    s[j],s[j+1]=s[j+1],s[j]
                    minSteps+=1
        return minSteps
        


    if __name__ == '__main__':
       solution = example('','100')
       print(solution)
       