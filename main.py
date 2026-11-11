#https://github.com/ArmitaJF85/Vehicle-Management
class Vehicle:
    def init(self, id, model, color, price, is_sold):
        self.id = id
        self.model = model
        self.color = color
        self.price = price
        self.is_sold = is_sold

    def update_price(self, new_price):
        self.price = new_price

    def update_sold_status(self, status):
        self.is_sold = status

    def get_info(self):
        sold = "Yes" if self.is_sold else "No"
        return f"ID: {self.id} | Model: {self.model} | Color: {self.color} | Price: {self.price} | Sold: {sold}"


class Car(Vehicle):
    def init(self, id, model, color, price, is_sold, number_of_doors):
        super().init(id, model, color, price, is_sold)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"Car | {super().get_info()} | Doors: {self.number_of_doors}"


class Motorcycle(Vehicle):
    def init(self, id, model, color, price, is_sold, engine_capacity):
        super().init(id, model, color, price, is_sold)
        self.engine_capacity = engine_capacity

    def get_info(self):
        return f"Motorcycle | {super().get_info()} | Engine Capacity: {self.engine_capacity}"


class Truck(Vehicle):
    def init(self, id, model, color, price, is_sold, cargo_capacity):
        super().init(id, model, color, price, is_sold)
        self.cargo_capacity = cargo_capacity

    def get_info(self):
        return f"Truck | {super().get_info()} | Cargo Capacity: {self.cargo_capacity}"


n = int(input())
vehicles = {}

for _ in range(n):
    data = input().split()

    vehicle_type = data[0]
    id = int(data[1])
    model = data[2]
    color = data[3]
    price = int(data[4])
    is_sold = data[5] == "True"
    extra = int(data[6])

    if vehicle_type == "Car":
        vehicle = Car(id, model, color, price, is_sold, extra)
    elif vehicle_type == "Motorcycle":
        vehicle = Motorcycle(id, model, color, price, is_sold, extra)
    else:
        vehicle = Truck(id, model, color, price, is_sold, extra)

    vehicles[id] = vehicle


q = int(input())

for _ in range(q):
    command = input().split()

    if command[0] == "INFO":
        id = int(command[1])
        print(vehicles[id].get_info())

    elif command[0] == "PRICE":
        id = int(command[1])
        new_price = int(command[2])
        vehicles[id].update_price(new_price)

    elif command[0] == "SOLD":
        id = int(command[1])
        status = command[2] == "True"
        vehicles[id].update_sold_status(status)

