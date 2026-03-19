class Example:
    def example(self, s: str) -> int:
        count = 0
        if(len(s)==1):
            return ord(s)
        
        for i in range(len(s)):
            if(i+1!=len(s)):
                count += abs(ord(s[i])-ord(s[i+1]))
                
                
        return count


    if __name__ == '__main__':
       solution = example('','hello')
       print(solution)