passengers_counter=0

class Passenger:
    WEIGTH=75

    def __init__(self, target_floor):
        global passengers_counter
        passengers_counter+=1
        self.id=passengers_counter

        self.target_floor = target_floor

        self.wait_time=0.0
        self.move_time=0.0


    def add_wait_time(self, step):
        self.wait_time+=step
    
    def add_move_time(self, step):
        self.move_time+=step


    def __str__(self):
        return "Пассажир %d, Время ожидания: %f Время поездки: %f" % (
            self.id,
            self.wait_time, 
            self.move_time
            )
