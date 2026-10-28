# Case 8 - Problem 64: Tuple-Based Course Registration Validation

registrations = []
n = int(input("Number of registration records: "))
valid = n >= 0

for i in range(n):
    student = input("Student ID: ").strip()
    course = input("Course code: ").strip().upper()
    credits = int(input("Credits: "))

    if student == "" or course == "" or credits <= 0:
        print("Invalid registration")
        valid = False
        break
    registrations.append((student, course, credits))

if valid:
    seen = []
    student_ids = []
    student_credits = []
    duplicate_found = False

    for rec in registrations:
        student, course, credits = rec
        key = (student, course)
        if key in seen:
            print("Duplicate registration:", student, "-", course)
            duplicate_found = True
        else:
            seen.append(key)
            if student not in student_ids:
                student_ids.append(student)
                student_credits.append(credits)
            else:
                idx = student_ids.index(student)
                student_credits[idx] = student_credits[idx] + credits

    if not duplicate_found:
        print("No duplicate registrations")

    print("Credit totals by student:")
    for i in range(len(student_ids)):
        print(student_ids[i], ":", student_credits[i])
