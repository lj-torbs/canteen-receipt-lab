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


print("Costumer:", first_name.title(), last_name.title())
print("Item:", item.title(), f"x{qty}")

price = float(price_text.replace("P", "").replace(",", "").replace("p", ""))

subtotal = round(price * qty, 2)

clean_type = customer_type.strip().lower()
if clean_type == "student":
    discount = subtotal * 0.10
elif clean_type == "senior" or clean_type == "pwd":
    discount = subtotal * 0.20
else:
    discount = 0.0
    
discount = round(discount, 2)
payable = round(subtotal - discount, 2)

vat = round(payable * 0.12, 2)
total = round(payable + vat, 2)
change = round(payment - total, 2)

total_centavos = round(change * 100)
pesos = total_centavos // 100
centavos = total_centavos % 100

print(f"Subtotal: {subtotal:.2f}")
print(f"VAT (12%): {vat:.2f}")
print(f"Total: {total:.2f}")
if payment < payable:
    print("Insufficient Payment")
else:
    print(f"Paid: {payment:.2f}")
    print(f"Change: {pesos} pesos and {centavos} centavos")