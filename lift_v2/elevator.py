from button import Button
from floor import Floor

class Elevator:
    def __init__(self, index, floor):
        self.id = index
        self.max_weight = 500
        self.cur_floor = floor
        self.cur_passengers = []
        self.is_elevator_up = False #Button()
        self.is_elevator_down =False #Button()

    def move_to(self, new_floor: Floor):
        self.cur_floor = new_floor

    def set_max_number_of_passengers(self, max_passengers):
        self.max_weight = max_passengers*75

    def get_count_of_passengers(self):
        return len(self.cur_passengers)

    # def set_current_floor(self, new_current_floor):
    #     self.cur_floor = new_current_floor

    def get_obj_of_passengers_target_floors(self):
        #для получения списка объектов целевых этажей пассажиров лифта
        return [p.target_floor for p in self.cur_passengers]

    def get_numbers_of_passengers_target_floors(self):
        #для получения списка номеров целевых этажей пассажиров лифта
        passengers_target_floors = self.get_obj_of_passengers_target_floors()
        floors_number = [st.number for st in passengers_target_floors]
        return floors_number

    def reset_direction(self):
        self.is_elevator_up=False#.change_state(False)
        self.is_elevator_down=False#.change_state(False)

    def get_actual_target_floor(self, floors_objs):
        #Метод, определяющий этаж, на который должен двигаться лифт

        def identify_target_floor(pos_targets):
            # Сравнение этажей по разнице между номером текущего этажа и цели из списка целей (min)
            actual_target_floor = min(pos_targets, 
                                key=lambda f: abs(self.cur_floor.number - f.number)
                                )
            return actual_target_floor

        # Формирование списка из целевых этажей пассажиров, находящихся в лифте
        possible_targets = self.get_obj_of_passengers_target_floors()
        if possible_targets:
            # Определение ближайшего этажа из списка целей
            actual_target_floor = identify_target_floor(possible_targets)
        else:
            # Если задания нет (лифт пуст), то лифт остается на текущем этаже
            actual_target_floor = self.cur_floor
            possible_targets = []
            for obj in floors_objs:
                # Если на этажах остались пассажиры, то лифт отправиться к ближайшему этажу
                if obj.get_count_of_passengers() >= 1:
                    possible_targets.append(obj)
                    actual_target_floor = identify_target_floor(possible_targets)

        return actual_target_floor

    def get_path(self, floors_objs):
        #Метод, определяющий путь лифта

        actual_target = self.get_actual_target_floor(floors_objs)
        # Если целевой этаж ниже текущего
        if self.cur_floor.number > actual_target.number:
            lift_path = floors_objs[actual_target.number - 1:self.cur_floor.number - 1]
            # Инвертировать путь
            lift_path.reverse()
            # Направление движения лифта - Вниз
            self.is_elevator_up=False#.change_state(False)
            self.is_elevator_down=True#.change_state(True)

        # Если целевой этаж выше текущего
        elif self.cur_floor.number < actual_target.number:
            lift_path = floors_objs[self.cur_floor.number:actual_target.number]
            # Направление движения лифта - Вверх
            self.is_elevator_up=True#.change_state(True)
            self.is_elevator_down=False#.change_state(False)

        # Если нет целей
        else:
            lift_path = [actual_target]
            # Направление движения лифта - нет направления
            self.is_elevator_up=False#.change_state(False)
            self.is_elevator_down=False#.change_state(False)

        return lift_path

    def redefine_direction(self, floors_objs):
        """ Метод, переопределяющий направление движения лифта """

        actual_target = self.get_actual_target_floor(floors_objs)
        # Если целевой этаж ниже текущего
        if self.cur_floor.number > actual_target.number:
            # Направление движения лифта - Вниз
            self.is_elevator_up=False#.change_state(False)
            self.is_elevator_down=True#.change_state(True)

        # Если целевой этаж выше текущего
        elif self.cur_floor.number < actual_target.number:
            # Направление движения лифта - Вверх
            self.is_elevator_up=True#.change_state(True)
            self.is_elevator_down=False#.change_state(False)

        # Если нет целей
        else:
            # Направление движения лифта - нет направления
            self.is_elevator_up=False#.change_state(False)
            self.is_elevator_down=False#.change_state(False)

    def admit_passengers(self):
        """ Метод, добавляющий пассажиров в лифт (этаж -> лифт) !!! """

        diffc = self.max_weight - len(self.cur_passengers)*75
        new_ps = []
        # Если есть места, то пассажиры добавляются в лифт - вызывается метод класса Stage - get_passengers_list
        if diffc > 0:
            new_ps = self.cur_floor.get_passengers_list(diffc, 
                                                        self.cur_floor,
                                                        self.is_elevator_up,#.get_state(),
                                                        self.is_elevator_down#.get_state()
                                                        )  # !!!
            self.cur_passengers += new_ps
            # Пассажиры, добавленные в лифт, удаляются с этажа
            self.cur_floor.remove_passengers(new_ps)

        return [ps_ts.target_floor.number for ps_ts in new_ps]

    def release_passengers(self):
        """ Метод, удаляющий пассажиров из лифта (лифт -> этаж) """

        cur_passengers_tmp = self.cur_passengers[:]
        removed_passengers = []
        for psgr in self.cur_passengers:
            if psgr.target_floor == self.cur_floor:
                removed_passengers.append(psgr)
                cur_passengers_tmp.remove(psgr)

        self.cur_passengers = cur_passengers_tmp

        return [ps_ts.target_floor.number for ps_ts in removed_passengers]

    def __str__(self):
        return 'Лифт %s - На этаже: %s, Пассажиры: %s : цели : %s' % (
            self.id, self.cur_floor.number,
            len(self.cur_passengers),
            self.get_numbers_of_passengers_target_floors()
        )
