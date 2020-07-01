def Factorial(number):
    fact = 1
    if number == 0:
        pass
    else:
        for i in range (1,number+1):
            fact *= i
    return fact



def Calculate_Result(num1, operator, num2):
    num1 = float(num1)
    try:
        num2 = float(num2)
        # Two number operations
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '%':
            result = num1 * num2 / 100
        elif operator == '**':
            result == num1 ** num2
        elif operator == '//':
            result = 'Q:  '+ str(num1//num2) + "  R:  "+ str(num1%num2) 
        else:
            result = 'Invalid operation'
    except ValueError:
        result = "Please Enter a Valid Number"
    else:
        result = "Whoops"

    if operator == '!':
        result = Factorial(num1)
    else:
        pass

    return result

 