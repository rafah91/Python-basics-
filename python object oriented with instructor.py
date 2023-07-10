class Calc:
    
    def mysum(self,x,y):
        print(x+y)

    def mymul(self,x,y):
        print(x*y)
    #constructor
    def __init__(self):
        print('welcome')
        
c1 = Calc()
c1.mysum(5,10)
c1.mymul(10,20)
    
