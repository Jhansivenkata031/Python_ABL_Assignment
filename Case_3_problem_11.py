# Case 3 - Problem 11: Examination Result and Grace-Mark Validation

marks = []
valid = True

for i in range(5):
    mark = int(input("Enter marks for subject " + str(i + 1) + ": "))
    if mark < 0 or mark > 100:
        print("Invalid mark. Marks must be 0 to 100.")
        valid = False
        break
    marks.append(mark)

if valid:
    failed = []
    for i in range(5):
        if marks[i] < 35:
            failed.append(i)

    if len(failed) == 0:
        result = "PASS"
    elif len(failed) == 1 and 30 <= marks[failed[0]] <= 34:
        index = failed[0]
        needed = 35 - marks[index]
        marks[index] = marks[index] + needed
        result = "PASS WITH " + str(needed) + " GRACE MARKS"
    else:
        result = "FAIL"

    print("Final marks:", marks)
    print("Result:", result)
