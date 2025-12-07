class flight:
    def __init__ ( self, code, seats, price):
        self.code = code
        self.seats = seats
        self.price = price

class flightbookingsystem:
    def __init__ (self):
        self.flights = {}
        self.ticket_id = 1

    def add_flight(self, code , seats , price):
        self.flights [code] = flight(code , seats , price)
    def view_flights(self):
        for f in self.flights.values():
            print (f"{f.code} | seats left : {f.seats} | Price:${f.price}")

    def book_seat(self,code):
        if code in self.flights and self.flights[code].seats>0:
         self.flights[code].seats -=1
         print(" Seat booked")
         return self.flights[code].price
        else:
            print( "Not Available")
            return None
    def pay(self, amount):
        print(f"payment of ${amount}succesful!")
    def generate_ticket(self,flight_code,amount):
        print("\n TICKET RECEIPT")
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Flight Code:{flight_code}")
        print(f"Amount Paid :${amount}")
        print("Status : Confirmed")
        print("=======")
        self.ticket_id +=1
system = flightbookingsystem()

while True:
    print("1. Add flight")
    print("2. View flights")
    print("3. Book and pay")
    print("4. Exit")

    ch = input("select option:")
    if ch == "1":
        code = input("Enter flight code :")
        seats = int(input("enter total seats :"))
        price = int(input("Enter tickter price:$"))
        system.add_flight(code,seats,price)
    elif ch == "2":
        system.view_flights()
    elif ch =="3":
        code = input("enter flight code:")
        price = system.book_seat(code)
        if price:
            confirm = input(f"(pay ${price}?(y/n)):")
            if confirm.lower()=="y":
                system.pay(price)
                system.generate_ticket(code,price)
            else:
                print(f"payment canceled")
    elif ch =="4":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")