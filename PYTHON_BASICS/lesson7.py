#Unpacking a tuple
fruits = ("Oranges", "Lemon", "Berry")
(orange, green, red) = fruits

print(orange)
print(green)
print(red)

#Loop a tuple- same as list
for fruit in fruits:
    print(fruit)
print()

for i in range(len(fruits)):
    print(fruits[i])
print()

i = 0
while i < len(fruits):
    print(fruits[i])
    i = i+1

#Join - same as list
vegetables = ("Cabbage","Spinach", "Brocolli", "Sukuma")
joined_tuple = fruits + vegetables
print(joined_tuple)

####SETS#### -- does not allow duplicates-- order of items can change as you print --- to create empty_set use set()
set_one = {12, 33, 12, 14, 4 , 56, 78, 79}
print(type(set_one))
print(set_one)

empty_set = set()

#Add item to a set
set_one.add(100)
print(set_one)

#Update a set
list_items =["One", "Three", 23, 12]
set_one.update(list_items)
print(set_one)

#Remove an item from a set - discard()
set_one.discard("One")
print(set_one)

#Iterate over  set - same as tuple and list
for item in set_one:
    print(item)
print("Count of items in set_one: ", len(set_one))

#Set operations - union, intersection, difference, set difference
#Online shoppers - Electronics
sales_2022 = {"Samsung", "Von", "LG", "Sony", "Panasonic"}
sales_2023 = {"Ramtons", "Infix", "Samsung", "Sony", "Tecno"}

#----set union  sales_2022 or sales-2023
print("All items: ", sales_2022.union(sales_2023))
#----set intersection
print("Items in  both years: ", sales_2022.intersection(sales_2023))
#----set difference
print("Items bought in 2022 and not in 2023 or both: ", sales_2022.difference(sales_2023))
#----set symmetric difference
print("Items in 2022 and 2023 and not in the intersection: ", sales_2022.symmetric_difference(sales_2023))


#Check if sets are equal
setA = {2,3,4}
setB = {4,6,3}

if setA == setB:
    print("Set A and B are equal")
else:
    print("Set A and B are not equal")
