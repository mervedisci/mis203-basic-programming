def main():
    print("=== Savings Goal Planner ===")

    while True:
        try:
            starting_balance = float(input("Enter starting balance: "))
            if starting_balance < 0:
                print("Error: Starting balance cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            monthly_deposit = float(input("Enter monthly deposit: "))
            if monthly_deposit <= 0:
                print("Error: Monthly deposit must be positive. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            interest_rate = float(input("Enter monthly interest rate (%): "))
            if interest_rate < 0:
                print("Error: Interest rate cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            savings_goal = float(input("Enter savings goal: "))
            if savings_goal <= 0:
                print("Error: Savings goal must be positive. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    balance = starting_balance
    total_interest = 0.0
    months = 0

    if balance >= savings_goal:
        print(f"\nStarting balance ({balance:.2f}) already meets or exceeds the goal ({savings_goal:.2f}).")
        print("Goal reached in 0 months.")
        print(f"Final Balance: {balance:.2f}")
        print("Total Interest Earned: 0.00")
    else:
        print(f"\n{'Month':<8} | {'Interest Earned':<18} | {'New Balance':<12}")
        print("-" * 46)

        reached = False
        for m in range(1, 61):
            
            interest_earned = balance * interest_rate / 100.0
            total_interest += interest_earned
            balance += interest_earned
            balance += monthly_deposit
            
            months = m
            print(f"{months:<8} | ${interest_earned:<17.2f} | ${balance:<11.2f}")

            if balance >= savings_goal:
                reached = True
                break

        print("-" * 46)
        
        if reached:
            print(f"Success: Goal reached in {months} month(s)!")
        else:
            print("Goal not reached after 60 months.")

        print(f"Final Balance: {balance:.2f}")
        print(f"Total Interest Earned: {total_interest:.2f}")


if __name__ == "__main__":
    main()
