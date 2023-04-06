#create a list 5 marks
exam_marks = [43, 70, 51, 91, 32]

highest_mark = None
lowest_mark = None

#Find the highest mark
for marks in exam_marks:
    if highest_mark is None:
        highest_mark = marks
    elif highest_mark < marks:
        highest_mark = marks
    print("The highest mark is", highest_mark)
print()

#find the lowest mark
for marks in exam_marks:    
    if lowest_mark is None:
        lowest_mark = marks
    elif lowest_mark > marks:
        lowest_mark = marks
    print("The lowest mark is", lowest_mark)
print()

#find the average mark
count = 0
total = 0

for mark in exam_marks:
    count = count + 1
    total = total + mark
print("The total marks are:", total)
print("The average marks are:", total / count)
print()

#count the marks above and below 50
above_50 = 0
below_50 = 0

for mark in exam_marks:
    if mark < 50:
        below_50 = below_50 + 1
    else:
        above_50 = above_50 + 1
print("Marks below 50 are:", below_50)
print("Marks above 50 are:", above_50)
print()

#print pass or fail to the mark
for mark in exam_marks:
    if mark > 50:
        print(mark, "Pass")
    else:
        print(mark, "Fail")
