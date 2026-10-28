# Case 9 - Problem 1: University Scholarship Allocation

seats = int(input("Number of scholarships available: "))
n = int(input("Number of students: "))
students = []
valid = seats >= 0 and n >= 0

for i in range(n):
    sid = input("Student ID: ").strip()
    marks = float(input("Marks (0-100): "))
    income = float(input("Annual family income: "))

    if sid == "" or not (0 <= marks <= 100) or income < 0:
        print("Invalid student record")
        valid = False
        break
    students.append((sid, marks, income))

if valid:
    eligible = []
    for s in students:
        sid, marks, income = s
        if marks >= 85 and income <= 300000:
            eligible.append((-marks, income, sid, marks))

    eligible.sort()

    print("Scholarship ranking:")
    rank = 1
    awarded_count = 0
    for item in eligible:
        neg_m, income, sid, marks = item
        if rank <= seats:
            status = "AWARDED"
            awarded_count = awarded_count + 1
        else:
            status = "WAITLISTED / NOT AWARDED"
        print(rank, sid, marks, "Rs.", round(income, 2), status)
        rank = rank + 1

    if seats > awarded_count:
        unfilled = seats - awarded_count
    else:
        unfilled = 0

    print("Scholarships awarded:", awarded_count)
    print("Unfilled seats:", unfilled)
