class Car:
    def __init__(self,license,model,color) -> None:
        self.license = license
        self.model = model
        self.color = color
    def __repr__(self) -> str:
        return f"{self.license}, {self.model}, {self.color}"

class Garage:
    def __init__(self) -> None:
        self.car_added = []
        self.spot = 10
        self.car_infos = {}

    def spot_available(self):
        return f"Total Spots Available {self.spot}"

    def add_car_to_garage(self,car):
        self.spot_name = ['A1','B1','C1','D1','E1','F1','G1','H1','I1','J1']
        if self.spot > 0:
            user_data = str(car).split(',')
            self.spot -= 1
            self.car_added.append(user_data)
            self.car_infos = {'Tickets': [],'License':[],'Model':[],'Color':[]}
            ticket = ''
            for i, val in enumerate(self.car_added):
                ticket = self.spot_name[i] + val[0]
                self.car_infos['Tickets'].append(ticket)
                self.car_infos['License'].append(val[0])
                self.car_infos['Model'].append(val[1])
                self.car_infos['Color'].append(val[2])
            print(f"Successfully Parked!!! YOUR TICKET {ticket}")
        else:
            print("NO SPOTS AVAILABLE!!!!!!")

