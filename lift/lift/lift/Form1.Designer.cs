namespace lift {
    partial class Form1 {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing) {
            if (disposing && (components != null)) {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent() {
            this.components = new System.ComponentModel.Container();
            this.tbLog = new System.Windows.Forms.TextBox();
            this.pnNewPassenger = new System.Windows.Forms.Panel();
            this.btNewPassenger = new System.Windows.Forms.Button();
            this.nudToFloor = new System.Windows.Forms.NumericUpDown();
            this.lbToFloor = new System.Windows.Forms.Label();
            this.lbFromFloor = new System.Windows.Forms.Label();
            this.nudFromFloor = new System.Windows.Forms.NumericUpDown();
            this.tmTick = new System.Windows.Forms.Timer(this.components);
            this.lbAutor = new System.Windows.Forms.Label();
            this.btStop = new System.Windows.Forms.Button();
            this.btStart = new System.Windows.Forms.Button();
            this.pnNewPassenger.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nudToFloor)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudFromFloor)).BeginInit();
            this.SuspendLayout();
            // 
            // tbLog
            // 
            this.tbLog.Location = new System.Drawing.Point(41, 140);
            this.tbLog.Multiline = true;
            this.tbLog.Name = "tbLog";
            this.tbLog.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.tbLog.Size = new System.Drawing.Size(848, 265);
            this.tbLog.TabIndex = 0;
            // 
            // pnNewPassenger
            // 
            this.pnNewPassenger.Controls.Add(this.btNewPassenger);
            this.pnNewPassenger.Controls.Add(this.nudToFloor);
            this.pnNewPassenger.Controls.Add(this.lbToFloor);
            this.pnNewPassenger.Controls.Add(this.lbFromFloor);
            this.pnNewPassenger.Controls.Add(this.nudFromFloor);
            this.pnNewPassenger.Enabled = false;
            this.pnNewPassenger.Location = new System.Drawing.Point(41, 23);
            this.pnNewPassenger.Name = "pnNewPassenger";
            this.pnNewPassenger.Size = new System.Drawing.Size(456, 100);
            this.pnNewPassenger.TabIndex = 1;
            // 
            // btNewPassenger
            // 
            this.btNewPassenger.Location = new System.Drawing.Point(209, 30);
            this.btNewPassenger.Name = "btNewPassenger";
            this.btNewPassenger.Size = new System.Drawing.Size(202, 40);
            this.btNewPassenger.TabIndex = 4;
            this.btNewPassenger.Text = "Создать нового пассажира!";
            this.btNewPassenger.UseVisualStyleBackColor = true;
            // 
            // nudToFloor
            // 
            this.nudToFloor.Location = new System.Drawing.Point(137, 50);
            this.nudToFloor.Maximum = new decimal(new int[] {
            10,
            0,
            0,
            0});
            this.nudToFloor.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.nudToFloor.Name = "nudToFloor";
            this.nudToFloor.Size = new System.Drawing.Size(40, 20);
            this.nudToFloor.TabIndex = 3;
            this.nudToFloor.Value = new decimal(new int[] {
            5,
            0,
            0,
            0});
            // 
            // lbToFloor
            // 
            this.lbToFloor.AutoSize = true;
            this.lbToFloor.Location = new System.Drawing.Point(134, 17);
            this.lbToFloor.Name = "lbToFloor";
            this.lbToFloor.Size = new System.Drawing.Size(49, 13);
            this.lbToFloor.TabIndex = 2;
            this.lbToFloor.Text = "На этаж";
            // 
            // lbFromFloor
            // 
            this.lbFromFloor.AutoSize = true;
            this.lbFromFloor.Location = new System.Drawing.Point(23, 17);
            this.lbFromFloor.Name = "lbFromFloor";
            this.lbFromFloor.Size = new System.Drawing.Size(48, 13);
            this.lbFromFloor.TabIndex = 1;
            this.lbFromFloor.Text = "С этажа";
            // 
            // nudFromFloor
            // 
            this.nudFromFloor.Location = new System.Drawing.Point(26, 50);
            this.nudFromFloor.Maximum = new decimal(new int[] {
            10,
            0,
            0,
            0});
            this.nudFromFloor.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.nudFromFloor.Name = "nudFromFloor";
            this.nudFromFloor.Size = new System.Drawing.Size(40, 20);
            this.nudFromFloor.TabIndex = 0;
            this.nudFromFloor.Value = new decimal(new int[] {
            5,
            0,
            0,
            0});
            // 
            // tmTick
            // 
            this.tmTick.Interval = 1000;
            // 
            // lbAutor
            // 
            this.lbAutor.AutoSize = true;
            this.lbAutor.Location = new System.Drawing.Point(41, 425);
            this.lbAutor.Name = "lbAutor";
            this.lbAutor.Size = new System.Drawing.Size(185, 13);
            this.lbAutor.TabIndex = 2;
            this.lbAutor.Text = "Автор: Григорий Ильин ИУ7-88Б(В)";
            // 
            // btStop
            // 
            this.btStop.Enabled = false;
            this.btStop.Location = new System.Drawing.Point(677, 53);
            this.btStop.Name = "btStop";
            this.btStop.Size = new System.Drawing.Size(109, 40);
            this.btStop.TabIndex = 3;
            this.btStop.Text = "Стоп";
            this.btStop.UseVisualStyleBackColor = true;
            this.btStop.Click += new System.EventHandler(this.btStop_Click);
            // 
            // btStart
            // 
            this.btStart.Location = new System.Drawing.Point(533, 53);
            this.btStart.Name = "btStart";
            this.btStart.Size = new System.Drawing.Size(109, 40);
            this.btStart.TabIndex = 4;
            this.btStart.Text = "Старт";
            this.btStart.UseVisualStyleBackColor = true;
            this.btStart.Click += new System.EventHandler(this.btStart_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(935, 450);
            this.Controls.Add(this.btStart);
            this.Controls.Add(this.btStop);
            this.Controls.Add(this.lbAutor);
            this.Controls.Add(this.pnNewPassenger);
            this.Controls.Add(this.tbLog);
            this.Name = "Form1";
            this.Text = "Моделирование лифтов";
            this.pnNewPassenger.ResumeLayout(false);
            this.pnNewPassenger.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nudToFloor)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudFromFloor)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox tbLog;
        private System.Windows.Forms.Panel pnNewPassenger;
        private System.Windows.Forms.Button btNewPassenger;
        private System.Windows.Forms.NumericUpDown nudToFloor;
        private System.Windows.Forms.Label lbToFloor;
        private System.Windows.Forms.Label lbFromFloor;
        private System.Windows.Forms.NumericUpDown nudFromFloor;
        private System.Windows.Forms.Timer tmTick;
        private System.Windows.Forms.Label lbAutor;
        private System.Windows.Forms.Button btStop;
        private System.Windows.Forms.Button btStart;
    }
}

