# Case 10 - Problem 20: University Admission Decision Engine

seats = int(input("Available seats: "))
n = int(input("Number of applicants: "))
applicants = []
valid = seats >= 0 and n >= 0

for i in range(n):
    aid = input("Application ID: ").strip()
    entrance = float(input("Entrance score (0-100): "))
    qualifying = float(input("Qualifying percentage (0-100): "))

    if aid == "" or not (0 <= entrance <= 100) or not (0 <= qualifying <= 100):
        print("Invalid applicant data")
        valid = False
        break
    applicants.append((aid, entrance, qualifying))

if valid:
    eligible = []
    for a in applicants:
        aid, entrance, qualifying = a
        if entrance >= 70 and qualifying >= 60:
            eligible.append((-entrance, -qualifying, aid, entrance, qualifying))

    eligible.sort()

    print("Admission results:")
    rank = 1
    admitted_count = 0
    for item in eligible:
        neg_e, neg_q, aid, entrance, qualifying = item
        if rank <= seats:
            decision = "ADMITTED"
            admitted_count = admitted_count + 1
        else:
            decision = "WAITLISTED"
        print(rank, aid, entrance, qualifying, decision)
        rank = rank + 1

    if seats > admitted_count:
        rem_seats = seats - admitted_count
    else:
        rem_seats = 0

    print("Total admitted:", admitted_count)
    print("Seats remaining:", rem_seats)
