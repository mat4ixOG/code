class Example:
    def example(self, s: str) -> int:
        words = {'a':0 , 'b':0 , 'c':0}
        left = 0
        res = 0
        for right in range(len(s)):
            words[s[right]] += 1
            
            while all(words[char]>0 for char in 'abc'):
                res += len(s) - right
                words[s[left]] -= 1
                left += 1
                
        print (res)
                
        
        
        
               
                    
       


    if __name__ == '__main__':
       solution = example('',"abcabcabc")
       print(solution)