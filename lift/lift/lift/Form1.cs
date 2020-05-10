using lift.Properties;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace lift {
    public partial class Form1 : Form {
        public Form1() {
            InitializeComponent();
        }

        private void btStart_Click(object sender, EventArgs e) {
            btStart.Enabled = false;
            var bl = new BuildingLogic();
            pnNewPassenger.Enabled = true;
            tmTick.Enabled = true;
            btStop.Enabled = true;
        }

        private void btStop_Click(object sender, EventArgs e) {
            btStop.Enabled = false;
            pnNewPassenger.Enabled = false;
            tmTick.Enabled = false;

            //

            btStart.Enabled = true;
        }
    }
}
