def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x/y

def multiply(x, y):
    return x*y


if __name__ == "__main__":
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))

    choice = int(input("\nEnter your choice from below:\n1> Add \n2> Subtract \n3> Divide \n4> Multiply\n"))

    if choice==1:
        print("Ans is:",add(x,y))
    
    elif choice==2:
        print("Ans is:",sub(x,y))

    elif choice==3:
        print("Ans is:",divide(x,y))

    elif choice==4:
        print("Ans is:",multiply(x,y))

    else:
        print("Enter Valid Choice")