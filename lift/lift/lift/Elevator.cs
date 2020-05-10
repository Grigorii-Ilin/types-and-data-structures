using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lift {
    class Elevator {
        static int counter=0;//for id

        //public int FloorsCount { get; set; }

        const double maxWeigth=240.0;
        const double defaultSpeed = 0.1; //floors per second

        int id;
        ElevatorStates state = ElevatorStates.StayingClosed;
        bool[] buttons; //= new bool[FloorsCount];//pressed - True
        double weight = 0.0;
        double speed=0.0;
        double floor;

        public Elevator(double floor, int floorsCount) {

            this.buttons = new bool[floorsCount];
            for (int i = 0; i < this.buttons.Length; i++) {
                this.buttons[i] = false;
            }

            this.floor = floor;

            this.id=++counter;
        }
    }
}
