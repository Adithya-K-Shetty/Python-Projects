def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2 != 0:
        return n1/n2
    else:
        return "Enter A Non Zero Divisor..."

Calculate = True
Restart = True

while Calculate:
    num1 = int(input("What's The First Number : "))
    print('+ ->add\n- ->sub\n* ->mul\n/ ->div\n0->exit')
    while Restart:
        operator = input("Pick An Operation : ")
        if operator == '0':
            Calculate = False
            break
        num2 = int(input("What's The Next Number : "))
        if operator == '+':
            num1 = add(num1,num2)
            print("Result : ",num1)
        elif operator == '-':
            num1 = subtract(num1,num2)
            print("Result : ",num1)
        elif operator == '*':
            num1 = multiply(num1,num2)
            print("Result : ",num1)
        elif operator == '/':
            num1 = divide(num1,num2)
            print("Result : ",num1)
        else:
            print("Enter A Valid Operator")
            break
        restart_input = input("Type 'y' to continue calculating with "+str(num1)+", or type 'n' to start a new calculation : ")
        if restart_input == 'y':
            continue
        elif restart_input == 'n':
            break
    
