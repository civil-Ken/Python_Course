#num= 53
#if num> 55:
 #   print (num)
#else:
 #   print ("I don't know o!")
name= input("what is your name? ")
print ("welcome "+ name)
age= input("How old are you? ")
print ("I guess you were born in " , 2021 - int (age))
confirm= input("Am i right? ")
if confirm == ("yes") or ("yea"):
    print ("hurray!!")
else:
    print ("oh no!")
    print("I'm sorry, it should be ", 2020 - int (age))