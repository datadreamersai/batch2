# #Inheritance


class Vehicle():

    def __init__(self,no_of_tyres):
        self.no_of_tyres = no_of_tyres

    def start_engine(self):
        return "engine has started"

    def stop_engine(self):
        return "engine has stopped"
    
    def breaks(self):
        return "breaks applied"
    
    
    

class Honda(Vehicle):

    def music_system(self):
        return "JBL music system"

    def self_driviing(self):
        stop = super().stop_engine()
        return stop,"ADAS level2 feature"
    
    def start_engine(self):

        check_1=True
        check_2=True
        check_3=True
        if check_1==True& check_2==True & check_3==True:
            
            return super().stop_engine()
        
    def stop_engine(self):
        return "ldjfhkjsfghg"
    



h1 = Honda(4)
# print(h1.start_engine())
print(h1.self_driviing())






class Bank():

    def login(self):
        user_name = input("Please enter username:")
        password = input("Please enter password:")
        if (user_name=="datadreamers@gmail.com") & (password=="1234"):
            return True
        else:
            return False
        
    def loan(self):
        pass


class Axis(Bank):

    def login(self):
        if super().login()==True:
            otp = input("Please enter otp:")
            if otp=="1790":
                return "successfull login"
            else:
                return "AUthentication failed"
        else:
            return "AUthentication failed"
    
    def credit_card(self):
        pass


# a=Axis()
# print(a.login())
b=Bank()
print(b.login())




#method overloading

class Maths():

    def f1(self,*args):
        if len(args)==5:
            return sum(args)
        
        if len(args)==10:
            prod=1
            for i in args:
                prod=prod*i
            return prod
        


m=Maths()
print(m.f1(1,2,3,4,5,6,7,8,9,10))



#operator overloading

print(1+2)

print("data"+"_"+"dreamers")



