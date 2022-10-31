def calPoints(self, ops):
      stack = []
      for i in ops:
         if i == "+":
            first, second = stack[len(stack) - 1],
            stack[len(stack) - 2]
            stack.append(first + second)
         elif i == "D":
            stack.append(stack[-1] * 2)
         elif i == "C":
            stack.pop()
         else:
            stack.append(int(i))
      return sum(stack)