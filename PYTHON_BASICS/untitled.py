'''
print(Welcome to a guessing game, \n 
    You are allowed to enter number till it matches with the correct one)
counter = 0
while True:
    number = int(input("Enter a number: "))
    counter = counter + 1
    if number == 5:
        break
    print(number)
print('You made () attempts'.format(counter))
print('End of the game')
'''

'''
while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done")
'''

while True:
    password = input("Enter password: ")
    if password[0] == "#" or password[0] == "$" or password[0] == "%":
        print("First character correct.")
    else:
        print("First character wrong.")
        continue
    if password == "#python":
        print("Correct password")
        break
    else:
        print("Wrong password")
    print(password)
            
print("Logged in")
