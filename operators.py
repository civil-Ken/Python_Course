#Arithmetic operations
#print(59+84)
#print(298-38)
#print(5*2)
#print(34/4)
#print(34%4)
#print(34//4)
#print(4**8)
#comparison operators
#print ( 8 == 8)
#print( 2 == 4)
#print ( 10 > 11)
#print ( 34 >= 31)
#print ( 34 <= 31)
#logical operators
#print ( 5 == 5 and 3 == 3)
#print ( 5 == 5 and 3 == 2)
#print ( 5 == 5 or 3 == 2)
#print ( not True)

# Assignment operators
#x = 4 + 46
#print (x)

#x = 23
#x += 3
#print ( x )
#x = 5
#x /= 2
#print (x)
# CONDITIONAL OPERATORS
#name = "Kentosh"
#print ("False!" if name != "python" else "True!")
#x = 5 + 4
#print ( "True!" if "x = 9" else " false!" )
#print (bool(1), bool(0))


M= 65  #Area of reinforcements
b= 300
h= 600
F= 500
f= 25
c= 25
diameter= 16

d= (h-c-(diameter/2))
k= (M*(10**6))/(b*(d**2)*f)
z= d * (0.5+ ((0.25 - ( k /0.9 ) )** 0.5))
print (d,k,z)

print ("double reinforcement required" if  (z >= (d*0.95)) else "single reinforcement required")

Area = (M*(10**6))/(0.95*F*z)
print (Area)