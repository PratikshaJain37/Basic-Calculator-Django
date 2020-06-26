def help_calculate(num1, num2, operator):
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = (operator, type(operator))

    return result