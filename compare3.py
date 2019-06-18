a,b,c=0,0,0
def inputs():
         global a,b,c
         a=int(input("Enter first no."))
         b=int(input("Enter second no."))
         c=int(input("Enter third no."))
         return a,b,c
inputs()
if (a>=b):
         if(a>c):
                  print("The greatest no is ",a)
elif (b>=a):
         if(b>c):
                  print("The greatest no is ",b)
else:
         print("The greatest no is",c)
