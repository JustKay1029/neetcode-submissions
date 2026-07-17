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
                    res = a+b
                    operands.append(res)
                elif t == "-":
                    res = b - a
                    operands.append(res)
                elif t== "*":
                    res = a * b
                    operands.append(res)
                else:
                    try:
                        res = int(b /a)
                        operands.append(res)
                    except ZeroDivisionError:
                        print("Error: You cannot divide by zero.")
                        res = None

        return int(operands[0])
