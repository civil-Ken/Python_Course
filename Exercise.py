Weight= int(input ("Weight: "))
unit = print (input ("(K)g or (L)bs: "))
print ("Weight in Kgs: " , Weight/0.45 if unit == "k or K",  else "Weight in Lbs: ", Weight*0.45)