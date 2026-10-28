# Case 7 - Problem 58: Library Borrowing and Fine Reconciliation

n = int(input("Number of returned books: "))
total_fine = 0
valid = n >= 0

for i in range(n):
    late_days = int(input("Late days for book " + str(i + 1) + ": "))

    if late_days < 0:
        print("Late days cannot be negative")
        valid = False
        break
    elif late_days <= 5:
        fine = late_days * 2
    else:
        fine = 5 * 2 + (late_days - 5) * 5

    print("Fine for book " + str(i + 1) + ": Rs.", fine)
    total_fine = total_fine + fine

if valid:
    print("Total library fine: Rs.", total_fine)
