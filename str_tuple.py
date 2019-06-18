def inputs():
         n=[('a','b'),('c','d'),('e','f')]
         return n
def compute(n):
         for i in range(0,len(n)):
                  n[i]='='.join(n[i])
         m=tuple(n)
         return m
n=inputs()
m=compute(n)
print(';'.join(m))
