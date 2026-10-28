# Case 1 - Problem 2: Progressive Electricity Billing

units = float(input("Enter units consumed: "))

if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        energy_charge = units * 1.50
    elif units <= 200:
        energy_charge = 100 * 1.50 + (units - 100) * 2.50
    else:
        energy_charge = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00

    total_bill = energy_charge + 50
    print("Energy charge: Rs.", round(energy_charge, 2))
    print("Total bill: Rs.", round(total_bill, 2))
