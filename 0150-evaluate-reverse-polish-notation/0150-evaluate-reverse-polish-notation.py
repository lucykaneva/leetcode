class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operands = []
        
        for token in tokens:
            if token.isnumeric():
                operands.append(int(token))
            elif token[0] == '-' and token[1:].isnumeric():
                operands.append(int(token[1:])*(-1))
            else:
                operands.append(self.calculate(operands.pop(), operands.pop(), token))
        return operands[0]


        
    def calculate(self, a, b , operator):
        if operator == "+":
            return a+b
        elif operator == "-":
            return b-a
        elif operator == "*":
            return a*b
        else:
            return int(float(b) / a)