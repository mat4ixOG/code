from typing import Counter


class Example:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
         count = Counter(s)
         print(count)
        
        


    if __name__ == '__main__':
       solution = repeatLimitedString('','cczazcc',3)
       print(solution)