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

first_name = input()
last_name = input()
item = input()
price_text = input()
qty = int(input())
customer_type = input()
payment = float(input())


clean_first = first_name.strip().title()
clean_last = last_name.strip().title()
clean_item = item.strip().title()
clean_type = customer_type.strip().lower()

price = float(price_text.strip().lstrip("Pp₱"))
subtotal = round(price * qty, 2)

if clean_type == "student":
    discount_rate = 0.10
elif clean_type in ["senior", "pwd"]:
    discount_rate = 0.20
else:
    discount_rate = 0.0

discount = subtotal * discount_rate

if subtotal >= 500:
    discount += 25.00

discount = round(discount, 2)
discounted_amount = round(subtotal - discount, 2)

vat = round(discounted_amount * 0.12, 2)
total = round(discounted_amount + vat, 2)

print(f"Customer: {clean_first} {clean_last}")
print(f"Item: {clean_item} x{qty}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"VAT (12%): {vat:.2f}")
print(f"Total: {total:.2f}")

if payment < total:
    print("Insufficient payment")
else:
    print(f"Paid: {payment:.2f}")
    change = round(payment - total, 2)
    pesos = int(change)
    centavos = round((change - pesos) * 100)
    print(f"Change: {pesos} pesos and {centavos} centavos")
