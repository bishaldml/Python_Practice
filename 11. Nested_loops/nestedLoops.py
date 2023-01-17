symbol = input("Enter a symbol to use: ")
row = int(input("Enter the number of rows to use: "))
column = int(input("Enter the number of column to use: "))

for i in range(row):
    for j in range(column):
        print(symbol,end="")
    print()