import random

from button import Button
from passenger import Passenger

class Floor:

    def __init__(self, number):
        self.number = number
        self.max_num_of_passengers = 14
        self.passengers = []
        self.up_button = Button()
        self.down_button = Button()

    def reset_stage_buttons(self):
        self.up_button.change_state(False)
        self.down_button.change_state(False)

    def initialize_floor_buttons(self):
        self.reset_stage_buttons()
        if self.passengers:
            for p in self.passengers:
                if not self.up_button.is_enabled and p.target_floor.number > self.number:
                    self.up_button.change_state(True)
                elif not self.down_button.is_enabled and p.target_floor.number < self.number:
                    self.down_button.change_state(True)

                if self.up_button.is_enabled and self.down_button.is_enabled:
                    break

    def add_passengers(self, stages_list):
        diff = self.max_num_of_passengers - len(self.passengers)
        if diff > 0:
            # Объекту пассажира передается объект его целевого этажа с использованием модуля random
            nbuilding = stages_list[:]
            nbuilding.remove(self)  # Из списка исключается текущий этаж
            for _ in range(diff):
                self.passengers.append(Passenger(random.choice(nbuilding)))
        # Переинициализация состояния кнопок этажа
        self.initialize_floor_buttons()

    def remove_passengers(self, psgr_list):
        for psgr in psgr_list:
            self.passengers.remove(psgr)

        self.initialize_floor_buttons()

    def get_count_of_passengers(self):
        return len(self.passengers)

    def get_passengers_list(self, free_places, floor, up_elevator_state, down_elevator_state):
        #для получения списка объектов пассажиров, переходящих в лифт

        ps_list = self.passengers

        # При движении лифта вверх, на промежуточных этажах принимаются пассажиры, едущие вверх
        if up_elevator_state:
            ps_list = [ps for ps in self.passengers if ps.target_floor.number > floor.number]

        # При движении лифта вниз, на промежуточных этажах принимаются пассажиры, едущие вниз
        elif down_elevator_state:
            ps_list = [ps for ps in self.passengers if ps.target_floor.number < floor.number]

        return ps_list[:free_places], free_places>len(ps_list)

    def get_numbers_of_passengers_target_floors(self):
        return [p.target_floor.number for p in self.passengers]

    def __str__(self):
        return 'Этаж %s - Вверх: %s, Вниз: %s, Пассажиры: %s : Цели : %s' % (
            self.number, 
            self.up_button, 
            self.down_button, 
            self.get_count_of_passengers(),
            set(self.get_numbers_of_passengers_target_floors())
        )

