


# one = "1,191,200.13101880 PHP"
# two = "1,000.00 PHP"
#
#
# onecut = one.replace(',', '').replace(' PHP', '')
# twocut = two.replace(',', '').replace(' PHP', '')
# total = float(onecut) + float(twocut)

#print(f"{total:.8f}")
#
# totaldeposit = "1,025,571.92501880"
# three = "500.00"
#
# totalcut = totaldeposit.replace(',', '')
# threecut = three.replace(',', '')
#
# total = float(totalcut) + float(threecut)
#
# print(f"{total:.2f}")


# one =  "1,191,200.13101880 PHP"
# two = "0.0000 PHP"
#
# onecut = one.replace(',','').replace(' PHP', '')
# twocut = two.replace(',','').replace(' PHP', '')
#
# total = float(onecut) - float(twocut)
# print(total)

descriptTitle  = "Deposit No: 3057"
descripTitleCut = descriptTitle[len("Deposit No: "):]

print(descripTitleCut)