class Example:
    class Solution:
        def canChange(self, start: str, target: str) -> bool:
            
            start_pos = [(ch, i) for i, ch in enumerate(start) if ch != '_']
            target_pos = [(ch, i) for i, ch in enumerate(target) if ch != '_']

            if len(start_pos) != len(target_pos):
                return False

            for (start_ch, start_index), (target_ch, target_index) in zip(start_pos, target_pos):
                if start_ch != target_ch:
                    return False
                if start_ch == 'L' and start_index < target_index:
                    return False
                if start_ch == 'R' and start_index > target_index:
                    return False

            return True
          
if __name__ == '__main__':
    solution = Example.Solution()
    result = solution.canChange("_L__R__R_", "L______RR")
    print("Can Change:", result)
