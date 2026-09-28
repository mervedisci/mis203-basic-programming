item1 = input("Enter a item name: ")
qua1 = int(input("Enter quantitie: "))
price1 = int(input("Enter price: "))
item2 = input("Enter a another item name: ")
qua2 = int(input("Enter quantitie: "))
price2 = int(input("Enter price: "))
delivery_fee = float(input("Enter delivery fee: "))
tax_percent = float(input("Enter tax percentage: "))

subtotal = ( qua1 * price1 ) + (qua2 + price2)
tax_amount = subtotal * (tax_percent / 100)
final_total = subtotal + tax_amount + delivery_fee

print(f"Subtotal: {subtotal:2f} TL ")
print(f"Tax Percentage ({tax_percent}): {tax_amount:2f} ")
print(f"Delivery Fee: {delivery_fee:2f} TL ")
print(f"Final Total: {final_total:2f} TL ")
