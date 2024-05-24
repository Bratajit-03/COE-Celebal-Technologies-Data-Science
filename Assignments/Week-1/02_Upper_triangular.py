def upper_triangular(n):
    for i in range(n):
        for j in range(n):
            if j < i:
                print(' ', end=' ')
            else:
                print('*', end=' ')
        print()

if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    print("upper Triangular:")
    upper_triangular(n)
