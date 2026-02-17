def calculate(expression):
    expression = expression.replace(" ", "")  
    stack = []
    num = 0
    sign = '+'
    i = 0

    while i < len(expression):
        char = expression[i]

        
        if char.isdigit():
            num = num * 10 + int(char)
        if (not char.isdigit() and char != '-') or i == len(expression) - 1:
            
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] = stack[-1] * num
            elif sign == '/':
                stack[-1] = stack[-1] / num

            sign = char
            num = 0

        i += 1

    result = sum(stack)
    return round(float(result), 2)
