from typing import List


class Example:
 class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Brute Force Approach That takes all words then add (Passed 57 out of 66 test cases)
        #  space = ' '
        #  modWord = ''
        #  for i in range(len(s)):
        #      if i in spaces:
        #          modWord+= space +s[i]
        #      else:
        #          modWord+= s[i]
        #  return modWord
        
        #Splitting And Joining the string
        res = []
        prevIndex = 0
        for i in spaces:
            res.append(s[prevIndex:i])
            prevIndex = i
        res.append(s[prevIndex:])
        return ' '.join(res)
        


    if __name__ == '__main__':
       solution = addSpaces('','LeetcodeHelpsMeLearn',[8,13,15])
       print(solution)