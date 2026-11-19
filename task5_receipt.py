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

price_text.index[0:]
price = int(price_text)
sub_total = price * qty
Vat = sub_total % 12
total_final = sub_total + Vat
Change = payment - total_final
cent_avos = int((Change * 100) // 2 % 12)

if customer_type == "student":
    discount = payment % 10 
    payable = sub_total - discount 
elif customer_type == "senior":
    discount = payment % 20 
    payable = sub_total - discount 
if customer_type == "other customer":
    discount = 0 
    payable = sub_total - discount
elif payment > sub_total:
    pay = "OK"
else:
    pay = "Insufficient payment" 

 
print("Customer: " + first_name.strip().title() + " " + last_name.strip().title())
print("Item: " + item.title().strip() + " x", qty)  
print("Subtotal: " , sub_total, 2)
print("Discount: ", discount)
print("VAT (12%): ", Vat, 2)
print("Total: ", total_final, 2)
print("Paid: ", payment, 2)
print("Change: ", Change , " Pesos and " , cent_avos , " centavos")