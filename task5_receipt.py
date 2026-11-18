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

# TODO: write your code below


subtotal = round(price * qty, 2)
vat = round(subtotal * 0.12, 2)
total = round(subtotal + vat, 2)
paid = payment
change = round(paid - total, 2)
price = float(price_text.replace("P", "").replace(",", ""))
customer_type = customer_type.strip().lower() 

centavos = round(change * 100)
pesos = centavos // 100
remaining_centavos = centavos % 100

print("Customer: " + first_name.strip().title() + " " +  last_name.strip().title())
print("Item: " + item + "x" + qty)

if customer_type == "student":
    percentage_discount = subtotal * 0.10
elif customer_type == "senior" or customer_type == "pwd":
    percentage_discount = subtotal * 0.20
else:
    percentage_discount = 0

if subtotal >= 500:
    percentage_discount += 25

discount = round(percentage_discount, 2)
payable = round(subtotal - discount, 2)
print(f"Discount: {discount:.2f}")

print(f"VAT (12%): {vat:.2f}")
print(f"Total: {total:.2f}")
print(f"Paid: {paid:.2f}")
print(f"Change: {pesos} pesos and {remaining_centavos} centavos")