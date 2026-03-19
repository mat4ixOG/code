from typing import List


class Example:
    def removeDupes(self, nums: List[int]) -> int:
        dupes = set()
        for i in nums:
            if i not in dupes:
                dupes.add(i)
                
        print(list(dupes))
        pass
        


    if __name__ == '__main__':
       solution = removeDupes('',[0, 0, 3, 3, 5, 6])
       print(solution)