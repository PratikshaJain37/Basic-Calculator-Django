def Calculate_Result(num1, num2, operator):
    
    if operator == '+':
        result = float(num1) + float(num2)
    elif operator == '-':
        result = float(num1) - float(num2)
    elif operator == '*':
        result = float(num1) * float(num2)
    elif operator == '/':
        result = float(num1) / float(num2)
    else:
        result = 'invalid'

    return result