# Case 4 - Problem 53: Food Waste Monitoring System

prepared_total = 0.0
waste_total = 0.0
valid = True

meals = ["Breakfast", "Lunch", "Dinner"]
for meal in meals:
    prepared = float(input(meal + " prepared (kg): "))
    wasted = float(input(meal + " wasted (kg): "))

    if prepared < 0 or wasted < 0 or wasted > prepared:
        print("Invalid quantities")
        valid = False
        break

    prepared_total = prepared_total + prepared
    waste_total = waste_total + wasted

if valid:
    if prepared_total == 0:
        percentage = 0.0
    else:
        percentage = (waste_total / prepared_total) * 100

    if percentage < 10:
        category = "Low"
    elif percentage <= 25:
        category = "Moderate"
    else:
        category = "High"

    print("Total prepared:", round(prepared_total, 2), "kg")
    print("Total wasted:", round(waste_total, 2), "kg")
    print("Waste percentage:", round(percentage, 2), "%")
    print("Waste level:", category)
