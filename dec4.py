import string
class Example:
   class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        #Optimal
       alphaInc = {chr(i): chr(i + 1) for i in range(ord('a'), ord('z'))}
       alphaInc['z'] = 'a'
    
       n, m = len(str2), len(str1)
       i, j = 0, 0
    
       while i < n and j < m:
            if str2[i] == str1[j] or str2[i] == alphaInc[str1[j]]:
               i += 1
            j += 1
       return i == n
        
    if __name__ == '__main__':
       solution = canMakeSubsequence('','abc' , 'ad')
       #Output should be 1
       print(solution)

        # #Incrementing the word 
        # word = ''
        # alphaInc = {chr(i): chr(i + 1) for i in range(ord('a'), ord('z'))}
        # alphaInc['z'] = 'a'
        # for i in str1:
        #     word += alphaInc[i]
        # #Checking if str2 is a substring of word
        # word = str1
        # size1, size2 = len(str2),len(word)
        # i,j = 0 , 0
        # while i < size1 and j < size2:
        #     if str2[i] == word[j]:
        #         i += 1
        #     j += 1
        # return i == size1
        