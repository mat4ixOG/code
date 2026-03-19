from typing import List


class Example:
    def combinationSum(self, candidates: List[int], target: int) ->  List[List[int]]:
        res = []
        def backTrack(start , path ,remain):
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return
            
            for i in range(start , len(candidates)):
                path.append(candidates[i])
                backTrack(i , path , remain - candidates[i])
                path.pop()
                
        backTrack(0 , [] , target)
        return res
        


    if __name__ == '__main__':
       solution = combinationSum('',[2,3,6,7] , 7)
       print(solution)