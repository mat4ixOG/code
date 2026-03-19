class Example:
    def example(self, s: int) -> int:
        counPos = 0
        countNeg = 0
        for i in s:
            if i > 0:
                counPos += 1
            else:
                countNeg += 1
        return max(countNeg, counPos)
        


    if __name__ == '__main__':
       solution = example('',[-2,-1,-1,1,2,3])
       print(solution)