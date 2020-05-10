import os

from buiding_logic import Building_logic

if __name__ == "__main__":
    os.system("cls")

    released_passengers=Building_logic.run(floors_count=11, elevators_count=3) 
    
    print("~"*50)
    for p in released_passengers:
        print(p)
    print("Среднее время ожидания:",
        sum([p.wait_time for p in released_passengers])/len(released_passengers)
        )
    print("Среднее время поездки:",
        sum([p.move_time for p in released_passengers])/len(released_passengers)
        )
