import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run(script, *answers):
    """Run a student script, type the answers, return its non-empty output lines."""
    p = subprocess.run(
        [sys.executable, os.path.join(ROOT, script)],
        input="\n".join(str(a) for a in answers) + "\n",
        capture_output=True, text=True, timeout=5, cwd=ROOT,
    )
    return [line.strip() for line in p.stdout.splitlines() if line.strip()]


class Task1BugHunt(unittest.TestCase):
    def check(self, points, tier):
        self.assertEqual(run("task1_bughunt.py", points), [tier])

    def test_bronze_low(self): self.check(0, "Bronze")
    def test_bronze_edge(self): self.check(99, "Bronze")
    def test_silver_edge(self): self.check(100, "Silver")
    def test_silver_top(self): self.check(499, "Silver")
    def test_gold_edge(self): self.check(500, "Gold")
    def test_gold_high(self): self.check(1200, "Gold")


class Task2Strings(unittest.TestCase):
    A = ("  juan ", " CRUZ", " rice meal ", 2, "2024-1234")
    B = ("ana", "lim", "juice", 10, "12345")

    def line(self, i, a, b):
        self.assertEqual(run("task2_strings.py", *self.A)[i:i + 1], [a])
        self.assertEqual(run("task2_strings.py", *self.B)[i:i + 1], [b])

    def test_customer(self): self.line(0, "Customer: Juan Cruz", "Customer: Ana Lim")
    def test_initials(self): self.line(1, "Initials: J.C.", "Initials: A.L.")
    def test_item(self): self.line(2, "Item: Rice Meal x2", "Item: Juice x10")
    def test_id(self): self.line(3, "ID: ******234", "ID: **345")


class Task3Numbers(unittest.TestCase):
    A = ("P100", 2, 300)
    B = ("P1,250.50", 3, 5000)
    C = ("P99.99", 3, 500)

    def line(self, i, a, b, c):
        self.assertEqual(run("task3_numbers.py", *self.A)[i:i + 1], [a])
        self.assertEqual(run("task3_numbers.py", *self.B)[i:i + 1], [b])
        self.assertEqual(run("task3_numbers.py", *self.C)[i:i + 1], [c])

    def test_subtotal(self): self.line(0, "Subtotal: 200.00", "Subtotal: 3751.50", "Subtotal: 299.97")
    def test_vat(self): self.line(1, "VAT (12%): 24.00", "VAT (12%): 450.18", "VAT (12%): 36.00")
    def test_total(self): self.line(2, "Total: 224.00", "Total: 4201.68", "Total: 335.97")
    def test_paid(self): self.line(3, "Paid: 300.00", "Paid: 5000.00", "Paid: 500.00")
    def test_change(self):
        self.line(4, "Change: 76 pesos and 0 centavos", "Change: 798 pesos and 32 centavos",
                  "Change: 164 pesos and 3 centavos")


class Task4Conditions(unittest.TestCase):
    def check(self, answers, discount, payable, verdict):
        self.assertEqual(run("task4_conditions.py", *answers),
                         [f"Discount: {discount}", f"Payable: {payable}", verdict])

    def test_student(self): self.check(("student", 200, 300), "20.00", "180.00", "Payment OK")
    def test_senior_messy_text_short_payment(self): self.check((" SENIOR ", 200, 150), "40.00", "160.00", "Insufficient payment")
    def test_pwd_rounding(self): self.check(("pwd", 299.97, 300), "59.99", "239.98", "Payment OK")
    def test_regular_no_discount(self): self.check(("regular", 499.99, 500), "0.00", "499.99", "Payment OK")
    def test_extra_25_exact_payment(self): self.check(("regular", 500, 475), "25.00", "475.00", "Payment OK")
    def test_one_centavo_short(self): self.check(("regular", 500, 474.99), "25.00", "475.00", "Insufficient payment")
    def test_student_both_rules(self): self.check(("student", 600, 515), "85.00", "515.00", "Payment OK")
    def test_senior_both_rules_short(self): self.check(("Senior", 600, 400), "145.00", "455.00", "Insufficient payment")


class Task5Receipt(unittest.TestCase):
    def test_student_receipt(self):
        self.assertEqual(run("task5_receipt.py", "  juan ", " CRUZ", "burger", "P100", 2, "student", 300), [
            "Customer: Juan Cruz", "Item: Burger x2", "Subtotal: 200.00", "Discount: 20.00",
            "VAT (12%): 21.60", "Total: 201.60", "Paid: 300.00", "Change: 98 pesos and 40 centavos"])

    def test_big_order_both_discounts(self):
        self.assertEqual(run("task5_receipt.py", "ana", "lim", "rice meal", "P120", 5, "senior", 1000), [
            "Customer: Ana Lim", "Item: Rice Meal x5", "Subtotal: 600.00", "Discount: 145.00",
            "VAT (12%): 54.60", "Total: 509.60", "Paid: 1000.00", "Change: 490 pesos and 40 centavos"])

    def test_insufficient_payment(self):
        self.assertEqual(run("task5_receipt.py", "ben", "santos", "juice", "P35.50", 3, "regular", 100), [
            "Customer: Ben Santos", "Item: Juice x3", "Subtotal: 106.50", "Discount: 0.00",
            "VAT (12%): 12.78", "Total: 119.28", "Insufficient payment"])

    def test_rounding_case(self):
        self.assertEqual(run("task5_receipt.py", "cara", "diaz", "pasta", "P99.99", 3, "pwd", 300), [
            "Customer: Cara Diaz", "Item: Pasta x3", "Subtotal: 299.97", "Discount: 59.99",
            "VAT (12%): 28.80", "Total: 268.78", "Paid: 300.00", "Change: 31 pesos and 22 centavos"])


if __name__ == "__main__":
    unittest.main()
