# Case 2 - Problem 3: Hospital Billing and Patient Classification

room = float(input("Enter room charges: "))
consultation = float(input("Enter consultation fee: "))
medicine = float(input("Enter medicine cost: "))

if room < 0 or consultation < 0 or medicine < 0:
    print("Invalid charges")
else:
    total = room + consultation + medicine

    if total < 5000:
        category = "Low"
    elif total <= 15000:
        category = "Moderate"
    else:
        category = "High"

    print("Total hospital bill: Rs.", round(total, 2))
    print("Patient bill category:", category)
