def sum(a,b):
    c = a+b
    return c

def sub(a,b):
    c = a-b
    return c

def mul(a,b):
    c = a*b
    return c

def div(a,b):
    c = a/b
    return c

def sqrt(a):
    c = a**2
    return c

is_on = True

while is_on:
    print("\n")
    print("For addition - sum")
    print("For substraction - sub")
    print("For multiplication - mul")
    print("For division - div")
    print("For exit the code - exit")
    print("For square root - sqrt")

    func_name = input("Please enter the function name from the above list: ")
    
    if func_name == "exit":
        is_on = False
    else:
        if func_name == "sum":
            first_num = int(input("Please enter first number: "))
            second_num = int(input("Please enter second number: "))
            s = sum(first_num,second_num)
            print(f"The addition of two numbers = {s}")

        elif func_name == "sub":
            first_num = int(input("Please enter first number: "))
            second_num = int(input("Please enter second number: "))
            su = sub(first_num,second_num)
            print(f"The substraction of two numbers = {su}")

        elif func_name == "mul":
            first_num = int(input("Please enter first number: "))
            second_num = int(input("Please enter second number: "))
            m = mul(first_num,second_num)
            print(f"The multiplication of two numbers = {m}")

        elif func_name == "div":
            first_num = int(input("Please enter first number: "))
            second_num = int(input("Please enter second number: "))
            d = div(first_num,second_num)
            print(f"The division of two numbers = {d}")
        
        elif func_name == "sqrt":
            num = int(input("Please enter the number: "))
            sq = sqrt(num)
            print(f"The sqaure root of the number = {sq}")