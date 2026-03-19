class Solution:
    def checkBinary(self , s: str)-> bool:
        count = 0 
        for i in range(1, len(s)):
            if s[i] == "1" and s[i-1] == "0":
                count+=1
        if s[0] == "1":
            count +=1
        return count<=1


if __name__ == '__main__':
    s = Solution()
    print(s.checkBinary("1001"))
    print(s.checkBinary("110"))
    print(s.checkBinary("1"))
    print(s.checkBinary("10"))