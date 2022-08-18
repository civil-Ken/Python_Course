Weight= input("Weight: ")
Unit = input ("(K)g or (L)bs: ")
if Unit.upper() == "L" :
    print ("Weight in Kg: " + str(float(Weight) *0.45))
elif Unit.upper() =="K":
    print("Weight in Lbs: " + str(float(Weight)/0.45))
else:
    print("Error")


