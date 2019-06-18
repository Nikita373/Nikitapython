def inputs():
         a=int(input("Enter first no."))
         b=int(input("Enter first no."))
         return a,b
a,b=inputs()
if(a>b):
         print("{0} is greater than {1}".format(a,b))
elif(b>a):
         print("{0} is greater than {1}".format(b,a))
else:
         print("They are equal")
         
         
         
