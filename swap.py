def inputs():
         a=input("enter the list of nos with space in between").split()
         pos1=int(input("Enter position 1"))
         pos2=int(input("Enter position2"))
         return a,pos1,pos2

def compute(a,pos1,pos2):
         a[pos1-1],a[pos2-1]=a[pos2-1],a[pos1-1]
         return a

def output(a):
         print(a)
         
def main():
         a,pos1,pos2=inputs()
         compute(a,pos1,pos2)
         output(a)
         

main()
         
         
                  
         
         
