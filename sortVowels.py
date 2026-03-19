class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        vowels_char = [char for char in s if char in vowels]
        vowels_char.sort()
        
        
        res = []
        idx = 0
        for i in s:
            if i in vowels_char:
                res.append(vowels_char[idx])
                idx+=1
            else:
                res.append(i)
        return ''.join(res)
    
if __name__ == '__main__':
    s = Solution()
    res = s.sortVowels('lEetcOde')
    print(res)
    
    # consonants -- l , t ,c , d
    #vowels --- E  e    O   e
    # ord  ---  69 101  79  101
    
    # response --- > lE0tcede
    # lEOtcede