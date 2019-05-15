import operator

class Solution:
    def evalRPN(self, tokens):
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '/':
                    res = int(operator.truediv(int(a), int(b)))
                else:
                    res = eval(a + token + b)
                stack.append(str(res))
        return int(stack.pop())

				
			
if __name__ == '__main__':
	s = Solution()
	#test1 = ["2", "1", "+", "3", "*"]
	test2 = ["4", "13", "5", "/", "+"]
	test3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
	test4 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
	print(s.evalRPN(test4))
