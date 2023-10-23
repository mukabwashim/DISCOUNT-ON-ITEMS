#discount for items above 1000bob
amount=float(input("enter the amount"))
if amount >=1000:
    discount =0.05 * amount
    print("the discount is ",discount)
else:
    print ("no discount offered")
    
