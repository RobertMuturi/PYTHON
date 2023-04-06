#Loops -- for and while loops
#Finite loop -- has an end
#Infinite loop -- does not terminate unless you interrupt

#While Loop
'''
count = 5

#condition is checked ..... count > 0   -- Finite Loop
while count> 0 :
    print(count)
    count = count - 1
print(' Nothing more count!')
print(count)

# While loop --- Infinite loop
while count > 0 :
    print("Counting")
print('Call off')

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')

while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')

#Guessing game - Guess -- Lottery -- random 
print(" ---Welcome to a Guessing game----")
print(" #################################")
print("You are allowed enter any number")
print("The game ends when your entry matches the number in the draw")
print()
counter = 0
while True:
    number = int(input('Enter a number: '))
    counter = counter + 1
    if number  == 5:
        break #Note the use of break
    print(number)
    print()
print("You made {} attempts".format(counter))
print("--------------------------------")
print("End of the Game!")
'''

#Use continue in while loop
while True:
    line = input('> ')
    if line[0] == '#' : 
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')



