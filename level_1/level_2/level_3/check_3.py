class Vehicle_Levels:
    def __init__(self, usage='domestic'):
        self.usage = usage

    def mileage_calculator(self, distance, capacity):
        self.mileage = distance/capacity
        return self.mileage


class Dummy_Levels:
    def __init__(self, dummy):
        self.dummy = dummy

    def check_dummy(self, name):
        if name == self.dummy:
            return True
        return False