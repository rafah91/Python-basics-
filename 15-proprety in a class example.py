class Calc:
    total=0 #class value
    def sum(self,x,y):
        print(x+y)
c = Calc()
print(c.total)

c.total=100 #instance or object value
print(c.total)

del c.total
print(c.total)

del c.total
print(c.total)
