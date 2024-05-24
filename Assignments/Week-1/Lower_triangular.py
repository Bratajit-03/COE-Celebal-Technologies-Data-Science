def lower_triangular(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        print()

n = int(input("Enter number of rows: "))
lower_triangular(n)
