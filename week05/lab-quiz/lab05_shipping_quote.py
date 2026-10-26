def subtotal(quantity, price):
    return quantity * price

def discount_rate(subtotal):
    if subtotal >= 100:
        return 0.10
    return 0.0

def shipping_fee(subtotal):
    if subtotal >= 50:
        return 0.0
    return 10.0

def final_price(subtotal, discount_rate, shipping_fee):
    discount_amount = subtotal * discount_rate
    final_total = (subtotal - discount_amount) + shipping_fee
    return final_total

assert discount_rate(99.99) == 0.0, "Error: 99.99 should have 0% discount"

assert discount_rate(100.00) == 0.10, "Error: 100.00 should have 10% discount"

assert shipping_fee(49.99) == 10.0, "Error: Orders under $50 should cost $10 for shipping"

print("All assert checks passed successfully!\n")

print("--- Order 1 Details ---")
price_1 = 25.0
qty_1 = 3
sub1 = subtotal(price_1, qty_1)
disc1 = discount_rate(sub1)
ship1 = shipping_fee(sub1)
total1 = final_price(sub1, disc1, ship1)

print(f"Subtotal: ${sub1:.2f}")
print(f"Discount Rate: {disc1 * 100}%")
print(f"Shipping Fee: ${ship1:.2f}")
print(f"Final Total: ${total1:.2f}\n")

print("--- Order 2 Details ---")
price_2 = 50.0
qty_2 = 3
sub2 = subtotal(price_2, qty_2)
disc2 = discount_rate(sub2)
ship2 = shipping_fee(sub2)
total2 = final_price(sub2, disc2, ship2)

print(f"Subtotal: ${sub2:.2f}")
print(f"Discount Rate: {disc2 * 100}%")
print(f"Shipping Fee: ${ship2:.2f}")
print(f"Final Total: ${total2:.2f}")

#print and return
#return: sends data back to the program so you can use it in math or other functions
#print(): just shows text on the screen, but you can't use it in math.
