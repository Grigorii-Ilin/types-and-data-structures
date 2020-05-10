using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lift {
    class BuildingLogic {
        const int floorsCount = 10;

        List<Elevator> elevators;
        List<Passenger> passengers;
        List<FloorButton> floorButtons;

        public BuildingLogic() {        
            elevators = new List<Elevator>();
            elevators.Add(new Elevator(3.0, floorsCount));
            elevators.Add(new Elevator(6.0, floorsCount));
            elevators.Add(new Elevator(9.0, floorsCount));

            floorButtons = new List<FloorButton>();
            floorButtons.Add(new FloorButton(false, true));
            for (int i = 1; i < floorsCount-1; i++) {
                floorButtons.Add(new FloorButton(true, true));
            }
            floorButtons.Add(new FloorButton(true, false));

            passengers = new List<Passenger>();
        };
    }

}
