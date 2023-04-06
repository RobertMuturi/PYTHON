#NESTED FOR LOOPS
'''
employees = ["Jack", "Ann", "Ken", "Ben", "Cate"]
salaries = [10000, 30000, 60000, 90000, 40000]

for employee in employees:
    for salary in salaries:
        print("{} earns {}: ".format(employee, salary))


for i in range(3): # 0,1,2
    for j in range(3): # 0,1,2
        print(i, "x", j, "=" , i*j)
    print("")

#Create some pattern


# outer loop
for i in range(6):
    # inner loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')
'''   
first = [2, 4, 6]
second = [2, 4, 6]
for i in first:
    for j in second:
        if i == j:
            continue
        print(i, '*', j, '= ', i * j)
