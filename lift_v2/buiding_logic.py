import random

from elevator import Elevator
from floor import Floor

class Building_logic:
    def __init__(self, floors_count, elevators_count):

        self.floors_count = floors_count
        self.elevators_count = elevators_count
        self.floors = [Floor(number) for number in range(1, floors_count + 1)]
        self.elevators = [Elevator(ind, self.floors[0]) for ind in range(1, elevators_count + 1)]

        print(self)

    def add_floors_passengers(self):
        for f in self.floors:
            f.add_passengers(self.floors)

    def is_active_passengers(self):
        for f in self.floors:
            if f.get_count_of_passengers()>=1:
                return True

        for e in self.elevators:
            if e.get_count_of_passengers()>=1:
                return True

        return False


    @classmethod
    def run(cls, floors_count: int, elevators_count: int): 
        #Метод для инициализации здания и запуска его лифтов в работу

        step_str = ' '.join(['*'*20,' Минута %s ', '*'*20])
        lift_str = ' '.join(['-'*20,' Лифт %s ', '-'*20])

        building = cls(floors_count, elevators_count)
        floors = building.floors
        elevators = building.elevators

        for e in elevators:
            f=floors[random.randint(0, floors_count-1)]
            e.move_to(f)

        building.add_floors_passengers()

        minutes_counter = 0.0
        release_counter = 0 # Счетчик развезенных пассажиров


        while building.is_active_passengers(): #ГЛАВНЫЙ ЦИКЛ
            print(step_str % minutes_counter)
            print('')

            for e in elevators:
                # Инициализация списков для хранения принятых и выпущенных пассажиров
                admitted = []
                removed = []
                intermediate_admitted = []

                path = e.get_path(floors)  # Формирование пути
                step = None
                for step in path:
                    e.move_to(step)
                    break  # Минимальный шаг - перемещение на 1 этаж
                #e.move_to(path[0])

                # Если достигнут целевой этаж
                if step == path[-1]:
                    # Удаление пассажиров из лифта
                    removed = e.release_passengers()
                    # Увеличение счетчика развезенных пассажиров
                    release_counter += len(removed)
                    # Переопределение направления дальнейшего движения
                    e.redefine_direction(floors)
                    # Забор пассажиров по направлению движения
                    admitted = e.admit_passengers()

                # Если достигнут промежуточный этаж. Если на этаже нажата кнопка вызова(Наверх, Вниз),
                # определяющая направление, совпадающее с направлением движения лифта, то лифт остановится и
                # примет новых пассажиров (если есть места)
                elif (e.is_elevator_up is step.up_button.is_enabled) or \
                        (e.is_elevator_down is step.down_button.is_enabled):
                    intermediate_admitted = e.admit_passengers()

                print(lift_str % e.id)

                print(step)
                print(e, 
                    '. Едет на: %s этаж' % path[-1].number \
                    if step != path[-1] \
                    else '. Остановился на: %s этаже' % path[-1].number
                    )
                print('- %s' % removed) if removed else None
                print('+ %s - промежуточные пассажиры' % intermediate_admitted
                        if intermediate_admitted else '+ %s' % admitted) \
                    if admitted or intermediate_admitted \
                    else None
            print('\n')

            minutes_counter += 0.5
            minutes_counter=round(minutes_counter, 1)

        print('')
        print('Этажей: %d. Число лифтов: %d. Всего минут: %d. Развезено пассажиров: %d' % (
            floors_count, 
            elevators_count, 
            minutes_counter, 
            release_counter)
            )

    def __str__(self):
        return 'Здание - Этажей: %s, Лифтов: %s' % (self.floors_count, self.elevators_count)
