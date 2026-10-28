# Case 5 - Problem 21: Traffic Violation Penalty Calculator

count = int(input("How many violations? "))
base_total = 0
valid = count >= 0

for i in range(count):
    violation = input("Enter violation (no helmet/signal jump/overspeeding): ").strip().lower()
    if violation == "no helmet":
        fine = 1000
    elif violation == "signal jump":
        fine = 2000
    elif violation == "overspeeding":
        fine = 1500
    else:
        print("Unknown violation:", violation)
        valid = False
        break

    print("Fine: Rs.", fine)
    base_total = base_total + fine

if valid:
    if base_total > 3000:
        surcharge = base_total * 0.20
    else:
        surcharge = 0.0

    final_penalty = base_total + surcharge
    print("Base fine: Rs.", round(base_total, 2))
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Final penalty: Rs.", round(final_penalty, 2))
