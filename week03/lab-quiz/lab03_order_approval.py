print("=== Order System ===")

try:
    quantity = int(input("Enter quantity: "))
    stock = int(input("Enter stock: "))
    price = float(input("Enter price (TRY): "))
    is_member_input = input("Is member? (yes/no): ").strip().lower()
except ValueError:
    print("Error: Bad input.")
    exit()

is_member = is_member_input == "yes"

if quantity <= 0:
    print("Rejected: Quantity must be above 0.")
elif quantity > stock:
    print("Rejected: Not enough stock.")
elif price <= 0:
    print("Rejected: Price must be above 0.")
else:
  if is_member and price >= 500:
    final_price = price * 0.90
    reason = "Approved: 10% member discount applied."
  elif is_member:
    final_price = price
    reason = "Approved: Member price (no discount under 500 TRY)."
  else:
    final_price = price
    reason = "Approved: Regular price."
    
print(f"\nStatus: {reason}")
print(f"Final Price: {final_price:.2f} TRY")
