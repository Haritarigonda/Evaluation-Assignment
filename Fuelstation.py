class FuelStation:
    def __init__(self, diesel: int, petrol: int, electric: int):
        self.diesel = diesel
        self.petrol = petrol
        self.electric = electric
        self.diesel_slots = [False] * diesel
        self.petrol_slots = [False] * petrol
        self.electric_slots = [False] * electric

    def fuel_vehicle(self, fuel_type: str) -> bool:
        if fuel_type == "diesel":
            for i in range(len(self.diesel_slots)):
                if not self.diesel_slots[i]:
                    self.diesel_slots[i] = True
                    return True
            return False
        elif fuel_type == "petrol":
            for i in range(len(self.petrol_slots)):
                if not self.petrol_slots[i]:
                    self.petrol_slots[i] = True
                    return True
            return False
        elif fuel_type == "electric":
            for i in range(len(self.electric_slots)):
                if not self.electric_slots[i]:
                    self.electric_slots[i] = True
                    return True
            return False
        else:
            return False

    def open_fuel_slot(self, fuel_type: str) -> bool:
        if fuel_type == "diesel":
            if self.diesel == 0:
                return False
            for i in range(len(self.diesel_slots)):
                if self.diesel_slots[i]:
                    self.diesel_slots[i] = False
                    self.diesel -= 1
                    return True
            return False
        elif fuel_type == "petrol":
            if self.petrol == 0:
                return False
            for i in range(len(self.petrol_slots)):
                if self.petrol_slots[i]:
                    self.petrol_slots[i] = False
                    self.petrol -= 1
                    return True
            return False
        elif fuel_type == "electric":
            if self.electric == 0:
                return False
            for i in range(len(self.electric_slots)):
                if self.electric_slots[i]:
                    self.electric_slots[i] = False
                    self.electric -= 1
                    return True
            return False
        else:
            return False

fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
print(fuel_station.fuel_vehicle("diesel")) # true
print(fuel_station.fuel_vehicle("petrol")) # true
print(fuel_station.fuel_vehicle("diesel")) # true
print(fuel_station.fuel_vehicle("electric")) # true
print(fuel_station.fuel_vehicle("diesel")) # false
print(fuel_station.open_fuel_slot("diesel")) # true
print(fuel_station.fuel_vehicle("diesel")) # true
print(fuel_station.open_fuel_slot("electric")) # true
print(fuel_station.open_fuel_slot("electric")) # false