using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lift {
    enum ElevatorStates {
        StayingClosed,
        MovingUp,
        MovingDown,
        DoorsOpening,
        DoorsClosing,
        PassengersOutIn,
        Overload
    }
}
