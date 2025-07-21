#Inheritance


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