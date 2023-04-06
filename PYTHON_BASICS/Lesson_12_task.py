#Create a multiple table where the user inputs the number of rows and columns to be printed
rows = int(input("How many rows do you want? "))
columns = int(input("How many columns do you want? "))
table = ""

for i in range(rows):
    for j in range(columns):
        print(i * j, end="" )
    print()
