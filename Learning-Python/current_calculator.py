# V = float(input("Enter voltage: "))
# R = float(input("Enter resistance: "))

# while True:
#     if R == 0:
#         R = float(input("Resistance cannot be zero, enter again: "))
#     else:
#         break

# I = V/R

# print("Current value: {}".format(I))

#------------------------------------------
V = float(input("Enter voltage: "))

while True:
    try:
        R = float(input("Enter resistance: "))
        I = V/R
        break
    except ZeroDivisionError:
        print("Resistance cannot be zero!")

print("Current value: {}".format(I))