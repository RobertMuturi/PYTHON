#empty list about cars
cars = []

#check the number of cars in list
print(cars)

#user to input cars they know and add to list
for car in range(5):
    car = input("Enter a variety of cars: ")
    cars.append(car)
print(cars)

#delete last item in list by default
cars.pop()
print(cars)

#user to input data into a new created list
lorry = []

for truck in range(3):
    truck = input("Enter a variety of lorries: ")
    lorry.append(truck)

print(lorry)

#extend the second list with the first
lorry.extend(cars)
print(lorry)

#clear items in the second list
lorry.clear()
print(lorry)

#delete second list
del lorry

