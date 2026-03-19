from typing import List
import math


class Example:
    def example(self, exp: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for i in exp:
            if i not in operators:
                stack.append(int(i))
            elif i in operators:
                rightOperator = stack.pop()
                leftOperator = stack.pop()
                operator = i
                res = self.calcOperation(leftOperator, rightOperator, operator)
                stack.append(res)

        return round(stack[0])

    def calcOperation(self, leftOperator, rightOperator, operator):
        if operator == '+':
            return leftOperator + rightOperator
        elif operator == '-':
            return leftOperator - rightOperator
        elif operator == '*':
            return leftOperator * rightOperator
        elif operator == '/':
            return math.trunc(leftOperator / rightOperator)


if __name__ == '__main__':
    solution = Example().example(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"])  # Ans is 22
    print(solution)