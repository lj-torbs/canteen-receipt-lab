# Task 5: Put it all together (15 points)
#
# Combine your work from tasks 2, 3 and 4 into one receipt program. Copy and paste
# the parts you need from your own earlier files.
#
# The first seven lines read the input for you. Do not change them.
# Example, if the input is "  juan ", " CRUZ", burger, P100, 2, student and 300,
# the program must print EXACTLY these lines:
#
#     Customer: Juan Cruz
#     Item: Burger x2
#     Subtotal: 200.00
#     Discount: 20.00
#     VAT (12%): 21.60
#     Total: 201.60
#     Paid: 300.00
#     Change: 98 pesos and 40 centavos
#
# Notes:
#   Subtotal and discount work as in tasks 3 and 4.
#   VAT is 12% of the amount AFTER the discount.
#   Total = (subtotal - discount) + VAT, all rounded to 2 decimals.
#   If the payment is not enough, the last two lines are replaced by one line:
#       Insufficient payment
#
# RULE: never put text inside input(). The grader types the answers for you.

first_name = first_name.strip().title()
last_name = last_name.strip().title()
item = item.strip().title()

# Convert price into a number
price = float(price_text.replace("P", "").replace(",", ""))

# Calculate subtotal
subtotal = round(price * qty, 2)

# Format customer type
customer_type = customer_type.strip().lower()

# Calculate discount
if customer_type == "student":
    discount = subtotal * 0.10
elif customer_type == "senior" or customer_type == "pwd":
    discount = subtotal * 0.20
else:
    discount = 0

# Additional discount
if subtotal >= 500:
    discount += 25

discount = round(discount, 2)

# Calculate VAT after discount
vat = round((subtotal - discount) * 0.12, 2)

# Calculate total
total = round((subtotal - discount) + vat, 2)

# Check payment
if payment >= total:
    change = round(payment - total, 2)
    change_centavos = round(change * 100)

    pesos = change_centavos // 100
    centavos = change_centavos % 100

    print(f"Customer: {first_name} {last_name}")
    print(f"Item: {item} x{qty}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"VAT (12%): {vat:.2f}")
    print(f"Total: {total:.2f}")
    print(f"Paid: {payment:.2f}")
    print(f"Change: {pesos} pesos and {centavos} centavos")
else:
    print(f"Customer: {first_name} {last_name}")
    print(f"Item: {item} x{qty}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"VAT (12%): {vat:.2f}")
    print(f"Total: {total:.2f}")
    print("Insufficient payment")
