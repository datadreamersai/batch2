class Loan():
    def __init__(self):
        self.__r = 0.10

    def int_cal(self,p,t):
        return (p*t*self.__r)/100
    
    def set_r(self,new_r):
        self.__r = new_r
        return "interest got changed to:".format(self.__r)
    
    def get_r(self):
        return self.__r
    
    def chang_of_r(self,new_r):
        self.__r = new_r
        return self.__r

    

u1 = Loan()
print(u1.int_cal(500000,10))
u1.__r=0.15
print(u1.__r)
print(u1.int_cal(500000,10))