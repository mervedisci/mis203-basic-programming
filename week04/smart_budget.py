import datetime
import random

print("Smart Budget & Spending Analyst")

#datetime ile rapor tarihi ve zaman damgası
report_date = datetime.datetime.now()
print(f"Report Date: {report_date.strftime('%d.%m.%Y - %H:%M')}") #gün.ay.yıl - saat-dakika

#kullanıcıdan toplam bütçeyi alma
try:
    total_budget = float(input("\nEnter your total monthly budget: "))
except ValueError:
    total_budget = 1000.0  #hatalı giriş olursa varsayılan değer

#harcamaları toplamak için bir döngü ve liste
expenses = []
print("\nPlease enter the amounts for this month's 3 main expense categories:")
categories = ["Rent/Bills", "Food/Grocery", "Entertainment/Social"]

for category in categories:
    while True:
        try:
            amount = float(input(f"-> What is your expense for {category} "))
            if amount < 0:
                print("Expense cannot be negative! Try again.")
                continue
            expenses.append(amount)
            break
        except ValueError:
            print("Please enter a valid number!")

#hesaplamalar
total_expense = sum(expenses)
remaining_money = total_budget - total_expense
expense_rate = (total_expense / total_budget) * 100 if total_budget > 0 else 0

#sürpriz finansal olay
surprise_events = [
    ("Unexpected Repair / Bill Expense ", -200),
    ("Lucky Cashback / Refund ", 150),
    ("Forgotten Small Side Income ", 75),
    ("No Surprise Events This Month ", 0)
]

selected_event_text, event_amount = random.choice(surprise_events)
updated_budget = total_budget + event_amount
remaining_balance = updated_budget - total_expense

#Sonuç / Özet raporu
print("\n" + "=" * 55)
print("ADVANCED FINANCIAL SURPRISE REPORT")
print("=" * 55)
print(f"Initial Budget:        ${total_budget:.2f}")
print(f"Surprise Event:        {selected_event_text} (${event_amount:+d})")
print(f"Updated Budget:        ${updated_budget:.2f}")
print(f"Total Expenses:        ${total_expense:.2f}")
print(f"Net Remaining Balance: ${remaining_balance:.2f}")

print("=" * 55)
