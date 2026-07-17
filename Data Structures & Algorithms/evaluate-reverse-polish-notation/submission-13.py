class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        operators = ["+","-","*","/"]
        for t in tokens:
            res = 0
            if t not in operators:
                operands.append(int(t))
            else:
                a = operands.pop()
                b = operands.pop()
                if t == "+":
                    operands.append(a+b)
                elif t == "-":
                    operands.append(b - a)
                elif t== "*":
                    operands.append(a * b)
                else:
                    try:
                        operands.append(int(b/a))
                    except ZeroDivisionError:
                        print("Error: You cannot divide by zero.")
                        res = None

        return int(operands[0])
