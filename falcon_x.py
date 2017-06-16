from random import randint

total_seats = 0
price = 1000
    
passenger_list = []
passenger_dict = {}


# Method to let staff create new seats
def create_seats(number_of_seats):
    total_seats = number_of_seats
# x = {}
# x[key] = value

def update_price(new_price):
    price = new_price


def book_seat(name):
    ticket_id = randint(1, total_seats)
    passenger_dict.update({"Ticket ID": ticket_id, "Name": name})
    
    passenger_list.append(passenger_dict)


def passenger_manifests(passenger_list):
    for i in passenger_list:
        print(i["Ticket ID"]+ ':' + i["Name"])
 