namespace TestVideo
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.toolStrip = new System.Windows.Forms.ToolStrip();
            this.cmbShutter = new System.Windows.Forms.ToolStripComboBox();
            this.cmbGain = new System.Windows.Forms.ToolStripComboBox();
            this.gbPosition = new System.Windows.Forms.GroupBox();
            this.lblPositionY = new System.Windows.Forms.Label();
            this.lblPositionX = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.gbPeak = new System.Windows.Forms.GroupBox();
            this.lblPeakY = new System.Windows.Forms.Label();
            this.lblPeakX = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.gbWidth = new System.Windows.Forms.GroupBox();
            this.lblGaussCorrelatW = new System.Windows.Forms.Label();
            this.lblGaussCorrelatV = new System.Windows.Forms.Label();
            this.label17 = new System.Windows.Forms.Label();
            this.label16 = new System.Windows.Forms.Label();
            this.label15 = new System.Windows.Forms.Label();
            this.label14 = new System.Windows.Forms.Label();
            this.label13 = new System.Windows.Forms.Label();
            this.lblWidthGaussW0 = new System.Windows.Forms.Label();
            this.lblWidthGaussW1 = new System.Windows.Forms.Label();
            this.lblWidthGaussW2 = new System.Windows.Forms.Label();
            this.lblWidthGaussV0 = new System.Windows.Forms.Label();
            this.lblWidthGaussV1 = new System.Windows.Forms.Label();
            this.lblWidthGaussV2 = new System.Windows.Forms.Label();
            this.lblLevel0 = new System.Windows.Forms.Label();
            this.lblWidthV0 = new System.Windows.Forms.Label();
            this.lblWidthW0 = new System.Windows.Forms.Label();
            this.lblLevel1 = new System.Windows.Forms.Label();
            this.lblWidthV1 = new System.Windows.Forms.Label();
            this.lblWidthW1 = new System.Windows.Forms.Label();
            this.lblLevel2 = new System.Windows.Forms.Label();
            this.lblWidthV2 = new System.Windows.Forms.Label();
            this.lblWidthW2 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.gbBucketType = new System.Windows.Forms.GroupBox();
            this.radioButtonRectangle = new System.Windows.Forms.RadioButton();
            this.radioButtonEllipse = new System.Windows.Forms.RadioButton();
            this.radioButtonCircle = new System.Windows.Forms.RadioButton();
            this.labelDiametrB = new System.Windows.Forms.Label();
            this.labelDiametrA = new System.Windows.Forms.Label();
            this.groupBoxBucketSize = new System.Windows.Forms.GroupBox();
            this.label10 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.groupBoxEnergy = new System.Windows.Forms.GroupBox();
            this.numericUpDownEnergy = new System.Windows.Forms.NumericUpDown();
            this.groupBoxPowerBucket = new System.Windows.Forms.GroupBox();
            this.checkBoxPowerBucket = new System.Windows.Forms.CheckBox();
            this.doVideo0 = new DOVideoWCL.DOVideo();
            this.toolStrip.SuspendLayout();
            this.gbPosition.SuspendLayout();
            this.gbPeak.SuspendLayout();
            this.gbWidth.SuspendLayout();
            this.gbBucketType.SuspendLayout();
            this.groupBoxBucketSize.SuspendLayout();
            this.groupBoxEnergy.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownEnergy)).BeginInit();
            this.groupBoxPowerBucket.SuspendLayout();
            this.SuspendLayout();
            // 
            // toolStrip
            // 
            this.toolStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.cmbShutter,
            this.cmbGain});
            this.toolStrip.Location = new System.Drawing.Point(0, 0);
            this.toolStrip.Name = "toolStrip";
            this.toolStrip.Size = new System.Drawing.Size(1205, 25);
            this.toolStrip.TabIndex = 1;
            this.toolStrip.Text = "toolStrip";
            // 
            // cmbShutter
            // 
            this.cmbShutter.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbShutter.Name = "cmbShutter";
            this.cmbShutter.Size = new System.Drawing.Size(121, 25);
            this.cmbShutter.SelectedIndexChanged += new System.EventHandler(this.cmbShutter_SelectedIndexChanged);
            // 
            // cmbGain
            // 
            this.cmbGain.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cmbGain.Name = "cmbGain";
            this.cmbGain.Size = new System.Drawing.Size(121, 25);
            this.cmbGain.SelectedIndexChanged += new System.EventHandler(this.cmbGain_SelectedIndexChanged);
            // 
            // gbPosition
            // 
            this.gbPosition.Controls.Add(this.lblPositionY);
            this.gbPosition.Controls.Add(this.lblPositionX);
            this.gbPosition.Controls.Add(this.label2);
            this.gbPosition.Controls.Add(this.label1);
            this.gbPosition.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.gbPosition.Location = new System.Drawing.Point(764, 28);
            this.gbPosition.Name = "gbPosition";
            this.gbPosition.Size = new System.Drawing.Size(212, 136);
            this.gbPosition.TabIndex = 2;
            this.gbPosition.TabStop = false;
            this.gbPosition.Text = "Position (µm)";
            // 
            // lblPositionY
            // 
            this.lblPositionY.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblPositionY.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblPositionY.Location = new System.Drawing.Point(53, 82);
            this.lblPositionY.Name = "lblPositionY";
            this.lblPositionY.Size = new System.Drawing.Size(129, 31);
            this.lblPositionY.TabIndex = 3;
            this.lblPositionY.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblPositionX
            // 
            this.lblPositionX.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblPositionX.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblPositionX.Location = new System.Drawing.Point(53, 37);
            this.lblPositionX.Name = "lblPositionX";
            this.lblPositionX.Size = new System.Drawing.Size(129, 31);
            this.lblPositionX.TabIndex = 2;
            this.lblPositionX.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label2
            // 
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label2.Location = new System.Drawing.Point(8, 83);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(31, 34);
            this.label2.TabIndex = 1;
            this.label2.Text = "Y";
            // 
            // label1
            // 
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label1.Location = new System.Drawing.Point(8, 35);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(31, 34);
            this.label1.TabIndex = 0;
            this.label1.Text = "X";
            // 
            // gbPeak
            // 
            this.gbPeak.Controls.Add(this.lblPeakY);
            this.gbPeak.Controls.Add(this.lblPeakX);
            this.gbPeak.Controls.Add(this.label6);
            this.gbPeak.Controls.Add(this.label7);
            this.gbPeak.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.gbPeak.Location = new System.Drawing.Point(982, 28);
            this.gbPeak.Name = "gbPeak";
            this.gbPeak.Size = new System.Drawing.Size(223, 136);
            this.gbPeak.TabIndex = 3;
            this.gbPeak.TabStop = false;
            this.gbPeak.Text = "Peak (µm)";
            // 
            // lblPeakY
            // 
            this.lblPeakY.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblPeakY.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblPeakY.Location = new System.Drawing.Point(55, 83);
            this.lblPeakY.Name = "lblPeakY";
            this.lblPeakY.Size = new System.Drawing.Size(129, 31);
            this.lblPeakY.TabIndex = 3;
            this.lblPeakY.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblPeakX
            // 
            this.lblPeakX.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblPeakX.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblPeakX.Location = new System.Drawing.Point(55, 38);
            this.lblPeakX.Name = "lblPeakX";
            this.lblPeakX.Size = new System.Drawing.Size(129, 31);
            this.lblPeakX.TabIndex = 2;
            this.lblPeakX.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label6
            // 
            this.label6.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label6.Location = new System.Drawing.Point(10, 84);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(31, 34);
            this.label6.TabIndex = 1;
            this.label6.Text = "Y";
            // 
            // label7
            // 
            this.label7.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label7.Location = new System.Drawing.Point(10, 36);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(31, 34);
            this.label7.TabIndex = 0;
            this.label7.Text = "X";
            // 
            // gbWidth
            // 
            this.gbWidth.Controls.Add(this.lblGaussCorrelatW);
            this.gbWidth.Controls.Add(this.lblGaussCorrelatV);
            this.gbWidth.Controls.Add(this.label17);
            this.gbWidth.Controls.Add(this.label16);
            this.gbWidth.Controls.Add(this.label15);
            this.gbWidth.Controls.Add(this.label14);
            this.gbWidth.Controls.Add(this.label13);
            this.gbWidth.Controls.Add(this.lblWidthGaussW0);
            this.gbWidth.Controls.Add(this.lblWidthGaussW1);
            this.gbWidth.Controls.Add(this.lblWidthGaussW2);
            this.gbWidth.Controls.Add(this.lblWidthGaussV0);
            this.gbWidth.Controls.Add(this.lblWidthGaussV1);
            this.gbWidth.Controls.Add(this.lblWidthGaussV2);
            this.gbWidth.Controls.Add(this.lblLevel0);
            this.gbWidth.Controls.Add(this.lblWidthV0);
            this.gbWidth.Controls.Add(this.lblWidthW0);
            this.gbWidth.Controls.Add(this.lblLevel1);
            this.gbWidth.Controls.Add(this.lblWidthV1);
            this.gbWidth.Controls.Add(this.lblWidthW1);
            this.gbWidth.Controls.Add(this.lblLevel2);
            this.gbWidth.Controls.Add(this.lblWidthV2);
            this.gbWidth.Controls.Add(this.lblWidthW2);
            this.gbWidth.Controls.Add(this.label5);
            this.gbWidth.Controls.Add(this.label8);
            this.gbWidth.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.gbWidth.Location = new System.Drawing.Point(764, 170);
            this.gbWidth.Name = "gbWidth";
            this.gbWidth.Size = new System.Drawing.Size(441, 287);
            this.gbWidth.TabIndex = 4;
            this.gbWidth.TabStop = false;
            this.gbWidth.Text = "Width (µm)";
            // 
            // lblGaussCorrelatW
            // 
            this.lblGaussCorrelatW.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblGaussCorrelatW.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblGaussCorrelatW.Location = new System.Drawing.Point(337, 240);
            this.lblGaussCorrelatW.Name = "lblGaussCorrelatW";
            this.lblGaussCorrelatW.Size = new System.Drawing.Size(100, 31);
            this.lblGaussCorrelatW.TabIndex = 23;
            this.lblGaussCorrelatW.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblGaussCorrelatV
            // 
            this.lblGaussCorrelatV.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblGaussCorrelatV.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblGaussCorrelatV.Location = new System.Drawing.Point(6, 240);
            this.lblGaussCorrelatV.Name = "lblGaussCorrelatV";
            this.lblGaussCorrelatV.Size = new System.Drawing.Size(100, 31);
            this.lblGaussCorrelatV.TabIndex = 22;
            this.lblGaussCorrelatV.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label17
            // 
            this.label17.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label17.ForeColor = System.Drawing.Color.Blue;
            this.label17.Location = new System.Drawing.Point(150, 250);
            this.label17.Name = "label17";
            this.label17.Size = new System.Drawing.Size(137, 20);
            this.label17.TabIndex = 21;
            this.label17.Text = "Gauss Corr. (%)";
            this.label17.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label16
            // 
            this.label16.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label16.ForeColor = System.Drawing.Color.Red;
            this.label16.Location = new System.Drawing.Point(337, 46);
            this.label16.Name = "label16";
            this.label16.Size = new System.Drawing.Size(100, 20);
            this.label16.TabIndex = 20;
            this.label16.Text = "Gauss";
            this.label16.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label15
            // 
            this.label15.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label15.ForeColor = System.Drawing.Color.Red;
            this.label15.Location = new System.Drawing.Point(112, 46);
            this.label15.Name = "label15";
            this.label15.Size = new System.Drawing.Size(100, 20);
            this.label15.TabIndex = 19;
            this.label15.Text = "Gauss";
            this.label15.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label14
            // 
            this.label14.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label14.Location = new System.Drawing.Point(231, 46);
            this.label14.Name = "label14";
            this.label14.Size = new System.Drawing.Size(100, 20);
            this.label14.TabIndex = 18;
            this.label14.Text = "Beam";
            this.label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label13
            // 
            this.label13.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label13.Location = new System.Drawing.Point(6, 46);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(100, 20);
            this.label13.TabIndex = 17;
            this.label13.Text = "Beam";
            this.label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lblWidthGaussW0
            // 
            this.lblWidthGaussW0.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblWidthGaussW0.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblWidthGaussW0.Location = new System.Drawing.Point(337, 203);
            this.lblWidthGaussW0.Name = "lblWidthGaussW0";
            this.lblWidthGaussW0.Size = new System.Drawing.Size(100, 31);
            this.lblWidthGaussW0.TabIndex = 16;
            this.lblWidthGaussW0.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblWidthGaussW1
            // 
            this.lblWidthGaussW1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblWidthGaussW1.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblWidthGaussW1.Location = new System.Drawing.Point(337, 148);
            this.lblWidthGaussW1.Name = "lblWidthGaussW1";
            this.lblWidthGaussW1.Size = new System.Drawing.Size(100, 31);
            this.lblWidthGaussW1.TabIndex = 15;
            this.lblWidthGaussW1.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblWidthGaussW2
            // 
            this.lblWidthGaussW2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblWidthGaussW2.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblWidthGaussW2.Location = new System.Drawing.Point(337, 93);
            this.lblWidthGaussW2.Name = "lblWidthGaussW2";
            this.lblWidthGaussW2.Size = new System.Drawing.Size(100, 31);
            this.lblWidthGaussW2.TabIndex = 14;
            this.lblWidthGaussW2.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblWidthGaussV0
            // 
            this.lblWidthGaussV0.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblWidthGaussV0.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblWidthGaussV0.Location = new System.Drawing.Point(112, 203);
            this.lblWidthGaussV0.Name = "lblWidthGaussV0";
            this.lblWidthGaussV0.Size = new System.Drawing.Size(100, 31);
            this.lblWidthGaussV0.TabIndex = 13;
            this.lblWidthGaussV0.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblWidthGaussV1
            // 
            this.lblWidthGaussV1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblWidthGaussV1.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblWidthGaussV1.Location = new System.Drawing.Point(112, 148);
            this.lblWidthGaussV1.Name = "lblWidthGaussV1";
            this.lblWidthGaussV1.Size = new System.Drawing.Size(100, 31);
            this.lblWidthGaussV1.TabIndex = 12;
            this.lblWidthGaussV1.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblWidthGaussV2
            // 
            this.lblWidthGaussV2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblWidthGaussV2.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblWidthGaussV2.Location = new System.Drawing.Point(112, 93);
            this.lblWidthGaussV2.Name = "lblWidthGaussV2";
            this.lblWidthGaussV2.Size = new System.Drawing.Size(100, 31);
            this.lblWidthGaussV2.TabIndex = 11;
            this.lblWidthGaussV2.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblLevel0
            // 
            this.lblLevel0.Location = new System.Drawing.Point(6, 185);
            this.lblLevel0.Name = "lblLevel0";
            this.lblLevel0.Size = new System.Drawing.Size(431, 17);
            this.lblLevel0.TabIndex = 10;
            this.lblLevel0.Text = "80.0%";
            this.lblLevel0.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lblWidthV0
            // 
            this.lblWidthV0.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblWidthV0.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblWidthV0.Location = new System.Drawing.Point(6, 203);
            this.lblWidthV0.Name = "lblWidthV0";
            this.lblWidthV0.Size = new System.Drawing.Size(100, 31);
            this.lblWidthV0.TabIndex = 9;
            this.lblWidthV0.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblWidthW0
            // 
            this.lblWidthW0.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblWidthW0.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblWidthW0.Location = new System.Drawing.Point(231, 203);
            this.lblWidthW0.Name = "lblWidthW0";
            this.lblWidthW0.Size = new System.Drawing.Size(100, 31);
            this.lblWidthW0.TabIndex = 8;
            this.lblWidthW0.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblLevel1
            // 
            this.lblLevel1.Location = new System.Drawing.Point(6, 130);
            this.lblLevel1.Name = "lblLevel1";
            this.lblLevel1.Size = new System.Drawing.Size(431, 17);
            this.lblLevel1.TabIndex = 7;
            this.lblLevel1.Text = "80.0%";
            this.lblLevel1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lblWidthV1
            // 
            this.lblWidthV1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblWidthV1.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblWidthV1.Location = new System.Drawing.Point(6, 148);
            this.lblWidthV1.Name = "lblWidthV1";
            this.lblWidthV1.Size = new System.Drawing.Size(100, 31);
            this.lblWidthV1.TabIndex = 6;
            this.lblWidthV1.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblWidthW1
            // 
            this.lblWidthW1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblWidthW1.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblWidthW1.Location = new System.Drawing.Point(231, 148);
            this.lblWidthW1.Name = "lblWidthW1";
            this.lblWidthW1.Size = new System.Drawing.Size(100, 31);
            this.lblWidthW1.TabIndex = 5;
            this.lblWidthW1.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblLevel2
            // 
            this.lblLevel2.Location = new System.Drawing.Point(6, 75);
            this.lblLevel2.Name = "lblLevel2";
            this.lblLevel2.Size = new System.Drawing.Size(431, 17);
            this.lblLevel2.TabIndex = 4;
            this.lblLevel2.Text = "80.0%";
            this.lblLevel2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lblWidthV2
            // 
            this.lblWidthV2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblWidthV2.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblWidthV2.Location = new System.Drawing.Point(6, 93);
            this.lblWidthV2.Name = "lblWidthV2";
            this.lblWidthV2.Size = new System.Drawing.Size(100, 31);
            this.lblWidthV2.TabIndex = 3;
            this.lblWidthV2.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblWidthW2
            // 
            this.lblWidthW2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblWidthW2.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.lblWidthW2.Location = new System.Drawing.Point(231, 93);
            this.lblWidthW2.Name = "lblWidthW2";
            this.lblWidthW2.Size = new System.Drawing.Size(100, 31);
            this.lblWidthW2.TabIndex = 2;
            this.lblWidthW2.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label5
            // 
            this.label5.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label5.Location = new System.Drawing.Point(6, 25);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(206, 20);
            this.label5.TabIndex = 1;
            this.label5.Text = "Vertical";
            this.label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label8
            // 
            this.label8.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label8.Location = new System.Drawing.Point(227, 25);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(210, 20);
            this.label8.TabIndex = 0;
            this.label8.Text = "Horizontal";
            this.label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // gbBucketType
            // 
            this.gbBucketType.Controls.Add(this.radioButtonRectangle);
            this.gbBucketType.Controls.Add(this.radioButtonEllipse);
            this.gbBucketType.Controls.Add(this.radioButtonCircle);
            this.gbBucketType.Location = new System.Drawing.Point(6, 54);
            this.gbBucketType.Name = "gbBucketType";
            this.gbBucketType.Size = new System.Drawing.Size(83, 100);
            this.gbBucketType.TabIndex = 5;
            this.gbBucketType.TabStop = false;
            this.gbBucketType.Text = " Type";
            // 
            // radioButtonRectangle
            // 
            this.radioButtonRectangle.AutoSize = true;
            this.radioButtonRectangle.Location = new System.Drawing.Point(10, 69);
            this.radioButtonRectangle.Name = "radioButtonRectangle";
            this.radioButtonRectangle.Size = new System.Drawing.Size(74, 17);
            this.radioButtonRectangle.TabIndex = 2;
            this.radioButtonRectangle.TabStop = true;
            this.radioButtonRectangle.Text = "Rectangle";
            this.radioButtonRectangle.UseVisualStyleBackColor = true;
            this.radioButtonRectangle.CheckedChanged += new System.EventHandler(this.radioButtonBucketType_CheckedChanged);
            // 
            // radioButtonEllipse
            // 
            this.radioButtonEllipse.AutoSize = true;
            this.radioButtonEllipse.Location = new System.Drawing.Point(10, 44);
            this.radioButtonEllipse.Name = "radioButtonEllipse";
            this.radioButtonEllipse.Size = new System.Drawing.Size(55, 17);
            this.radioButtonEllipse.TabIndex = 1;
            this.radioButtonEllipse.TabStop = true;
            this.radioButtonEllipse.Text = "Ellipse";
            this.radioButtonEllipse.UseVisualStyleBackColor = true;
            this.radioButtonEllipse.CheckedChanged += new System.EventHandler(this.radioButtonBucketType_CheckedChanged);
            // 
            // radioButtonCircle
            // 
            this.radioButtonCircle.AutoSize = true;
            this.radioButtonCircle.Location = new System.Drawing.Point(10, 19);
            this.radioButtonCircle.Name = "radioButtonCircle";
            this.radioButtonCircle.Size = new System.Drawing.Size(51, 17);
            this.radioButtonCircle.TabIndex = 0;
            this.radioButtonCircle.TabStop = true;
            this.radioButtonCircle.Text = "Circle";
            this.radioButtonCircle.UseVisualStyleBackColor = true;
            this.radioButtonCircle.CheckedChanged += new System.EventHandler(this.radioButtonBucketType_CheckedChanged);
            // 
            // labelDiametrB
            // 
            this.labelDiametrB.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.labelDiametrB.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.labelDiametrB.Location = new System.Drawing.Point(119, 56);
            this.labelDiametrB.Name = "labelDiametrB";
            this.labelDiametrB.Size = new System.Drawing.Size(100, 31);
            this.labelDiametrB.TabIndex = 13;
            this.labelDiametrB.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // labelDiametrA
            // 
            this.labelDiametrA.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.labelDiametrA.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.labelDiametrA.Location = new System.Drawing.Point(119, 17);
            this.labelDiametrA.Name = "labelDiametrA";
            this.labelDiametrA.Size = new System.Drawing.Size(100, 31);
            this.labelDiametrA.TabIndex = 12;
            this.labelDiametrA.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // groupBoxBucketSize
            // 
            this.groupBoxBucketSize.Controls.Add(this.label10);
            this.groupBoxBucketSize.Controls.Add(this.label9);
            this.groupBoxBucketSize.Controls.Add(this.labelDiametrA);
            this.groupBoxBucketSize.Controls.Add(this.labelDiametrB);
            this.groupBoxBucketSize.Location = new System.Drawing.Point(199, 54);
            this.groupBoxBucketSize.Name = "groupBoxBucketSize";
            this.groupBoxBucketSize.Size = new System.Drawing.Size(236, 100);
            this.groupBoxBucketSize.TabIndex = 14;
            this.groupBoxBucketSize.TabStop = false;
            this.groupBoxBucketSize.Text = " Bucket Size ";
            // 
            // label10
            // 
            this.label10.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label10.Location = new System.Drawing.Point(13, 66);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(100, 20);
            this.label10.TabIndex = 19;
            this.label10.Text = "Diameter B";
            this.label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label9
            // 
            this.label9.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label9.Location = new System.Drawing.Point(13, 27);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(100, 20);
            this.label9.TabIndex = 18;
            this.label9.Text = "Diameter A";
            this.label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // groupBoxEnergy
            // 
            this.groupBoxEnergy.Controls.Add(this.numericUpDownEnergy);
            this.groupBoxEnergy.Location = new System.Drawing.Point(96, 54);
            this.groupBoxEnergy.Name = "groupBoxEnergy";
            this.groupBoxEnergy.Size = new System.Drawing.Size(91, 100);
            this.groupBoxEnergy.TabIndex = 15;
            this.groupBoxEnergy.TabStop = false;
            this.groupBoxEnergy.Text = " Energy (%) ";
            // 
            // numericUpDownEnergy
            // 
            this.numericUpDownEnergy.DecimalPlaces = 1;
            this.numericUpDownEnergy.Increment = new decimal(new int[] {
            5,
            0,
            0,
            65536});
            this.numericUpDownEnergy.Location = new System.Drawing.Point(11, 32);
            this.numericUpDownEnergy.Name = "numericUpDownEnergy";
            this.numericUpDownEnergy.Size = new System.Drawing.Size(68, 20);
            this.numericUpDownEnergy.TabIndex = 0;
            this.numericUpDownEnergy.ValueChanged += new System.EventHandler(this.numericUpDownEnergy_ValueChanged);
            // 
            // groupBoxPowerBucket
            // 
            this.groupBoxPowerBucket.Controls.Add(this.checkBoxPowerBucket);
            this.groupBoxPowerBucket.Controls.Add(this.gbBucketType);
            this.groupBoxPowerBucket.Controls.Add(this.groupBoxBucketSize);
            this.groupBoxPowerBucket.Controls.Add(this.groupBoxEnergy);
            this.groupBoxPowerBucket.Location = new System.Drawing.Point(764, 474);
            this.groupBoxPowerBucket.Name = "groupBoxPowerBucket";
            this.groupBoxPowerBucket.Size = new System.Drawing.Size(441, 160);
            this.groupBoxPowerBucket.TabIndex = 16;
            this.groupBoxPowerBucket.TabStop = false;
            this.groupBoxPowerBucket.Text = "Power Bucket";
            // 
            // checkBoxPowerBucket
            // 
            this.checkBoxPowerBucket.AutoSize = true;
            this.checkBoxPowerBucket.Location = new System.Drawing.Point(17, 21);
            this.checkBoxPowerBucket.Name = "checkBoxPowerBucket";
            this.checkBoxPowerBucket.Size = new System.Drawing.Size(40, 17);
            this.checkBoxPowerBucket.TabIndex = 16;
            this.checkBoxPowerBucket.Text = "On";
            this.checkBoxPowerBucket.UseVisualStyleBackColor = true;
            this.checkBoxPowerBucket.CheckedChanged += new System.EventHandler(this.checkBoxPowerBucket_CheckedChanged);
            // 
            // doVideo0
            // 
            this.doVideo0.ActiveDevice = ((ushort)(0));
            this.doVideo0.Average = ((ushort)(1));
            this.doVideo0.AverageEnable = false;
            this.doVideo0.AveragePicture = ((ushort)(1));
            this.doVideo0.AveragePictureEnable = false;
            this.doVideo0.BackColor = System.Drawing.Color.Black;
            this.doVideo0.BucketEnergy = 86.5F;
            this.doVideo0.CurrentDimension = DOVideoWCL.DOVideo.Dimension.d2D;
            this.doVideo0.CurrentDraw = DOVideoWCL.DOVideo.DrawLine.eNone;
            this.doVideo0.CurrentProfile = DOVideoWCL.DOVideo.TypeProfile.eSum;
            this.doVideo0.EnablePowerBucket = false;
            this.doVideo0.FocalLens = 10F;
            this.doVideo0.GainIndex = ((ushort)(0));
            this.doVideo0.IndexZoom = ((ushort)(0));
            this.doVideo0.Levels = new float[] {
        13.5F,
        50F,
        80F,
        0F};
            this.doVideo0.Location = new System.Drawing.Point(0, 0);
            this.doVideo0.Merger = ((ushort)(0));
            this.doVideo0.Name = "doVideo0";
            this.doVideo0.PowerBucket = DOVideoWCL.DOVideo.BucketType.eEllipse;
            this.doVideo0.ProjectionAngleRotation = ((short)(45));
            this.doVideo0.ProjectionAngleTilt = ((short)(45));
            this.doVideo0.ProjectionAutoRotation = DOVideoWCL.DOVideo.Auto.eOff;
            this.doVideo0.ProjectionStepRotation = ((short)(10));
            this.doVideo0.ProjectionWireDensity = ((short)(1));
            this.doVideo0.ShiftGainIndex = ((short)(0));
            this.doVideo0.Shutter = 0;
            this.doVideo0.Size = new System.Drawing.Size(550, 440);
            this.doVideo0.TabIndex = 17;
            this.doVideo0.Unit = DOVideoWCL.DOVideo.PositionUnits.eMilimetr;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1205, 635);
            this.Controls.Add(this.groupBoxPowerBucket);
            this.Controls.Add(this.gbWidth);
            this.Controls.Add(this.gbPeak);
            this.Controls.Add(this.gbPosition);
            this.Controls.Add(this.toolStrip);
            this.Controls.Add(this.doVideo0);
            this.DoubleBuffered = true;
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.Form1_Paint);
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.toolStrip.ResumeLayout(false);
            this.toolStrip.PerformLayout();
            this.gbPosition.ResumeLayout(false);
            this.gbPeak.ResumeLayout(false);
            this.gbWidth.ResumeLayout(false);
            this.gbBucketType.ResumeLayout(false);
            this.gbBucketType.PerformLayout();
            this.groupBoxBucketSize.ResumeLayout(false);
            this.groupBoxEnergy.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownEnergy)).EndInit();
            this.groupBoxPowerBucket.ResumeLayout(false);
            this.groupBoxPowerBucket.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private DOVideoWCL.DOVideo doVideo0;
        private System.Windows.Forms.ToolStrip toolStrip;
        private System.Windows.Forms.ToolStripComboBox cmbShutter;
        private System.Windows.Forms.ToolStripComboBox cmbGain;
        private System.Windows.Forms.GroupBox gbPosition;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblPositionY;
        private System.Windows.Forms.Label lblPositionX;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.GroupBox gbPeak;
        private System.Windows.Forms.Label lblPeakY;
        private System.Windows.Forms.Label lblPeakX;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.GroupBox gbWidth;
        private System.Windows.Forms.Label lblLevel2;
        private System.Windows.Forms.Label lblWidthV2;
        private System.Windows.Forms.Label lblWidthW2;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label lblLevel0;
        private System.Windows.Forms.Label lblWidthV0;
        private System.Windows.Forms.Label lblWidthW0;
        private System.Windows.Forms.Label lblLevel1;
        private System.Windows.Forms.Label lblWidthV1;
        private System.Windows.Forms.Label lblWidthW1;
        private System.Windows.Forms.Label lblWidthGaussW0;
        private System.Windows.Forms.Label lblWidthGaussW1;
        private System.Windows.Forms.Label lblWidthGaussW2;
        private System.Windows.Forms.Label lblWidthGaussV0;
        private System.Windows.Forms.Label lblWidthGaussV1;
        private System.Windows.Forms.Label lblWidthGaussV2;
        private System.Windows.Forms.Label lblGaussCorrelatV;
        private System.Windows.Forms.Label label17;
        private System.Windows.Forms.Label label16;
        private System.Windows.Forms.Label label15;
        private System.Windows.Forms.Label label14;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.Label lblGaussCorrelatW;
        private System.Windows.Forms.GroupBox gbBucketType;
        private System.Windows.Forms.RadioButton radioButtonRectangle;
        private System.Windows.Forms.RadioButton radioButtonEllipse;
        private System.Windows.Forms.RadioButton radioButtonCircle;
        private System.Windows.Forms.Label labelDiametrB;
        private System.Windows.Forms.Label labelDiametrA;
        private System.Windows.Forms.GroupBox groupBoxBucketSize;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.GroupBox groupBoxEnergy;
        private System.Windows.Forms.NumericUpDown numericUpDownEnergy;
        private System.Windows.Forms.GroupBox groupBoxPowerBucket;
        private System.Windows.Forms.CheckBox checkBoxPowerBucket;
    }
}

