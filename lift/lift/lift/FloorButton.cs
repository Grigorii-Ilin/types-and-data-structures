using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lift{
    class FloorButton {
        //static int counter = 0;//for id
        //int id;

        bool? pressedDown=null;
        bool? pressedUp=null;

        public FloorButton(bool isDown, bool isUp) {
            //this.id = ++counter;

            if (isDown) {
                pressedDown = false;
            }

            if (isUp) {
                pressedUp = false;
            }
        }
    }
}
