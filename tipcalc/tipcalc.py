#tip calculator
total = float(input("Enter the total:"))
tip_percent = float(input("Enter percentage of tip to add:"))
tip_amount = float(tip_percent / 100)
total = (tip_amount * total) + total
print("%.2f" % total)
# two decmial places --> %.2f


