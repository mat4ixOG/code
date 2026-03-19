class Example:
    def reverseBits(self, s: int) -> int:
        ans = 0
        while s > 0:
            ans <<= 1
            print("$$$", ans)
            if(s & 1) == 1:
                ans |=1

            s>>=1
        print("$$" , ans)
            

    if __name__ == '__main__':
       solution = reverseBits('',41000020)
       print(solution)