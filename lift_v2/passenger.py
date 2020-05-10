
class Passenger:
    WEIGTH=75

    def __init__(self, target_floor):
        self.target_floor = target_floor

    def __str__(self):
        return str(self.target_floor.number)
