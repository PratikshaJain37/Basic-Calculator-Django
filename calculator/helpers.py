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
    
    if num2:
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
            result = 'Invalid operation with 2 numbers'

    else:
        if operator == '!':
            if num1==int(num1):
                result = Factorial(int(num1))
            else:
                result = 'Invalid operation: Whole Numbers Only'
        else:
            result = 'Invalid operation with only 1 number'


    return result

 