#tip calculator
total = float(input("Enter the total:"))
tip_percent = float(input("Enter percentage of tip to add:"))
tip_amount = float(tip_percent / 100)
#float(tip_amount)
total = (tip_amount * total) + total
#round(total, 2)
print("%.2f" % total)
# two decmial places --> %.2f


