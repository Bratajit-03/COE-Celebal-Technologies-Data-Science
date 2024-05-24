def pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))

n = int(input("Enter number of rows: "))
print("Pyramid:")
pyramid(n)
