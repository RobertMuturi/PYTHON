campus = input("Are you from the main campus? Yes or No? ")
school = input("Are you from the school of Engineering? Yes or No? ")
calculus = input("Are you studying calculus? Yes or No? ")

if campus == "yes":
    if school == "yes":
        if calculus == "yes":
            print("This student is in the school of Eng. at the main campus studying calculus")
        else:
            print("This student is in the school of Eng. at the main campus but not studying calculus")
    else:
        print("This student is from the main campus but not from the school of Engineering")
else:
    print("This student is not from the main campus")
