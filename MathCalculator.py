while True:
    try:
        x = float(input("Please input your first number: "))
        y = float(input("Please input your second Number: "))
        operator = input("Please input which operator do you want to use(+,-,/,*,**):")

        addition = (x)+(y)
        minus = (x)-(y)
        multiplication= (x)*(y)
        division = (x)/(y)
        powers = (x)**(y)
        
        if isinstance(x, float) == True and isinstance(y, float) == True:
            if operator == "+":
                print(addition)
                break
            elif operator == "-":
                print(minus)
                break
            elif operator == "*":
                print(multiplication)
                break
            elif operator == "/":
                print(division)
                break
            elif operator == "**":
                print (powers)
                break
            else:
                print("Please input a proper mathematical operator: ")
    except ValueError:  
        print("Enter a valid input! ")