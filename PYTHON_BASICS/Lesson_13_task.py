#program to check if number has a raminder of three, is even or is odd.
remainders_of_three = []
evens = []
odds = []

for i in range(100):
    if i % 5 == 3:
        remainders_of_three.append(i)
    elif i % 2 == 0:
        evens.append(i)  
    elif i % 2 != 0:
        odds.append(i)
        
        
print(f"{remainders_of_three} has a remainder of 3")
print(f"{evens} is an even number")
print(f"{odds} is an odd number")
        
