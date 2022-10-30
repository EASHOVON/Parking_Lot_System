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

    

