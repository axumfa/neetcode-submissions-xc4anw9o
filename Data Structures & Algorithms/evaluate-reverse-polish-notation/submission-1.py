class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+': lambda a,b : a + b,
         '-' : lambda a,b : a- b,
         '/': lambda a,b : int(a/b),
         '*': lambda a,b : a * b}

        stack = []


        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(operators[token](b,a))

        return stack[0]

     