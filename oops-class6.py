from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass


#     def music(self):
#         return "music started"


# class Honda(Vehicle):

#     def breaks(self):
#         return "breaks applied"
        
#     def start(self):
#         return "engine started"
    
#     def stop(self):
#         return "engine stopped"
    



# h=Honda()
# print(h.start())
# print(h.stop())
# print(h.music())


# v=Vehicle()








# class Mobile(ABC):

#     @abstractmethod
#     def call(self):
#         pass

#     def wifi_connection(self):
#         return "wifi got connected"
    
# class Iphone(Mobile):
#     def bluetooth(self):
#         return "Bluetooth connected"
    
#     def call(self):
#         return "call got connected"
    
#     @abstractmethod
#     def airplanmode(self):
#         pass


# class Android(Iphone):

#     def playstore(self):
#         return "playstore"
    
#     def airplanmode(self):
#         return "airplane mode"


# a=Android()
# print(a.airplanmode())
# print(a.playstore())
# print(a.call())
# print(a.bluetooth())
# print(a.wifi_connection())



# i=Iphone()
# v=Mobile()





# class Mobile():

#     def call(self):
#         pass

#     def wifi_connection(self):
#         return "wifi got connected"
    

    
   
    

# m=Mobile()
# print(m.call())



class Car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass



class WolksWogon(Car):

    def music(self):
        return "music"
    
    def start(self):
        return "syart"
    
    def stop(self):
        return "stop"
    

w=WolksWogon()
print(w.start())
print(w.music())
print(w.stop())