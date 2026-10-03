tickets_sold = 0
total_revenue = 0.0
free_tickets = 0

while True:
    name = input("Customer name (q to quit): ").strip()
    if name.lower() == "q":
        break

    try:
        age = int(input("Age: ").strip())
    except ValueError:
        print("Invalid age.")
        continue

    if age < 0 or age > 120:
        print("Invalid age.")
        continue

    day = input("Day (weekday/weekend): ").strip().lower()
    if day not in ["weekday", "weekend"]:
        print("Invalid day.")
        continue

    is_student = input("Student (yes/no): ").strip().lower()
    if is_student not in ["yes", "no"]:
        print("Please answer yes or no.")
        continue

    if day == "weekday":
        base_price = 200.0
    else:
        base_price = 250.0

    if age < 6:
        discount = 1.00
        category = "Free"
    elif age >= 65:
        discount = 0.50
        category = "Senior"
    elif 6 <= age <= 12:
        discount = 0.40
        category = "Child"
    elif is_student == "yes" and age <= 25:
        discount = 0.30
        category = "Student"
    else:
        discount = 0.00
        category = "Standard"

    final_price = base_price * (1.00 - discount)

    print(f"{name}: {final_price:.2f} TRY ({category})")

    tickets_sold += 1
    total_revenue += final_price
    if discount == 1.00:
        free_tickets += 1

if tickets_sold == 0:
    print("No tickets sold.")
else:
    avg_price = total_revenue / tickets_sold
    print(f"Tickets sold: {tickets_sold}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average price: {avg_price:.2f} TRY")
    print(f"Free tickets: {free_tickets}")
