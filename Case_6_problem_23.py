# Case 6 - Problem 23: Student Timetable Conflict Detection

classes = []
n = int(input("Enter number of classes: "))
valid = n >= 0

for i in range(n):
    print("Class", i + 1)
    day = input("Day: ").strip().lower()
    subject = input("Subject: ").strip()
    start = int(input("Start hour (0-23): "))
    end = int(input("End hour (1-24): "))

    if not (0 <= start < end <= 24):
        print("Invalid time interval")
        valid = False
        break
    classes.append((day, start, end, subject))

if valid:
    found = False
    for i in range(n):
        for j in range(i + 1, n):
            d1, s1, e1, sub1 = classes[i]
            d2, s2, e2, sub2 = classes[j]
            if d1 == d2 and s1 < e2 and s2 < e1:
                print("Conflict:", sub1, "and", sub2, "on", d1)
                found = True

    if not found:
        print("No timetable conflicts")
