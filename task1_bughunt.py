# Task 1: Bug hunt (10 points)
#
# The canteen stamp card gives a tier based on points:
#     500 points or more  -> Gold
#     100 to 499 points   -> Silver
#     0 to 99 points      -> Bronze
#
# The program below was written by a tired classmate and it prints the wrong tier
# for some inputs. Run the tests, find the bug, and fix it.
#
# Your commit message must say what the bug was (example: "Fix tier bug: ...").

points = int(input())

if points >= 500 :
    print("Gold")
elif points >= 100:
    print("Silver")
else:
    print("Bronze")
