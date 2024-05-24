def lower_triangular(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        print()

if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    print("Lower triangular:")
    lower_triangular(n)
