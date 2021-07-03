# '''
# 1 2 3 4 5 6 7 8 9 10
# '''

# class Train:
#     def __init__(self, name, fare, seats):
#         self.name = name
#         self.fare = fare
#         self.seats = seats

#     def getStatus(self):
#         print("************")
#         print(f"The name of the train is {self.name}")
#         print(f"The seats available in the train are {self.seats}")
#         print("************")

#     def fareInfo(self):
#         print(f"The price of the ticket is: Rs {self.fare}")

#     def bookTicket(self):
#         if(self.seats>0):
#             print(f"Your ticket has been booked! Your seat number is {self.seats}")
#             self.seats = self.seats - 1
#         else:
#             print("Sorry this train is full! Kindly try in tatkal")

#     def cancelTicket(self, seatNo):
#         pass

# intercity = Train("Intercity Express: 14015", 90, 2)
# intercity.getStatus() 
# intercity.bookTicket()
# intercity.bookTicket()
# intercity.bookTicket()
# intercity.getStatus()





class Train:
    def __init__(self,name,fare,sheets):
        self.name=name
        self.fare=fare
        self.sheets=sheets

    def getStatus(self):
        print(f"the name of train is {self.name}")
        print(f"the seat availabele  of train is {self.sheets}") 
    
    def fareinfo(self):
        print(f"the price of ticket Rs.{self.fare}")
        
    def bookticekt(self):
        if(self.sheets>0):
            print(f"Your ticket is boocked{self.sheets}")
            self.sheets=self.sheets-1
        else:
            print("train is full!")
            
intercity=Train("Intecity Express: 14015",90,3)
intercity.getStatus()
intercity.bookticekt()
intercity.bookticekt()
intercity.bookticekt()
intercity.bookticekt()
intercity.bookticekt()
intercity.getStatus()
intercity.fareinfo()