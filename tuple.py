def inputs():
         n="a=b;c=d;e=f;g=h"
         return n
def compute(n):
         m=n.split(';')
         for i in range(len(m)):
                  m[i]=tuple(m[i].split('='))
         return m
def output(m):
         print(m)
def main():
         n=inputs()
         m=compute(n)
         output(m)
         
main()


