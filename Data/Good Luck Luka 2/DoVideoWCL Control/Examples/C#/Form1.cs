using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Threading;

namespace TestVideo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            doVideo0.OnNewDataReceved += new DOVideoWCL.DOVideo.NewDataReceved(doVideo_OnNewDataReceved);

            radioButtonCircle.Checked = (doVideo0.PowerBucket == DOVideoWCL.DOVideo.BucketType.eCircle);
            radioButtonEllipse.Checked = (doVideo0.PowerBucket == DOVideoWCL.DOVideo.BucketType.eEllipse);
            radioButtonRectangle.Checked = (doVideo0.PowerBucket == DOVideoWCL.DOVideo.BucketType.eRect);

            numericUpDownEnergy.Value = Convert.ToDecimal(doVideo0.BucketEnergy);
        }

        void doVideo_OnNewDataReceved(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ArrayList aDevices;

            if (DOVideoWCL.DOVideo.GetVideoDeviceArray(out aDevices) == true)
            {
                if (doVideo0.StartVideo(0) == true)
                {
                    String strSerialNumber = doVideo0.SerialNumber;

                    cmbShutter.Items.Clear();

                    if ((doVideo0.ShutterTable != null) && (doVideo0.GainTable.Length > 0))
                    {
                        for (int i = 0; i < doVideo0.ShutterTable.Length; i++)
                            cmbShutter.Items.Add(doVideo0.ShutterTable[i].ToString());

                        cmbShutter.SelectedIndex = 0;
                    }

                    cmbGain.Items.Clear();

                    if ((doVideo0.GainTable != null) && (doVideo0.ShutterTable.Length > 0))
                    {
                        for (int i = 0; i < doVideo0.GainTable.Length; i++)
                            cmbGain.Items.Add(doVideo0.GainTable[i].ToString());

                        cmbGain.SelectedIndex = 0;
                    }

                    checkBoxPowerBucket.Checked = doVideo0.EnablePowerBucket;
                }
                else
                    MessageBox.Show("The system does not detect video devices");
            }
            else
                MessageBox.Show("The system does not detect video devices");
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            doVideo0.StopVideo();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            PointF pos = (PointF)doVideo0.Position.GetValue(0);
            PointF peak = (PointF)doVideo0.Peak.GetValue(0);

            lblPositionX.Text = pos.X.ToString("f2");
            lblPositionY.Text = pos.Y.ToString("f2");
            lblPeakX.Text = peak.X.ToString("f2");
            lblPeakY.Text = peak.Y.ToString("f2");

            lblLevel0.Text = ((Single)doVideo0.Levels.GetValue(0)).ToString("f1") + "%";
            lblLevel1.Text = ((Single)doVideo0.Levels.GetValue(1)).ToString("f1") + "%";
            lblLevel2.Text = ((Single)doVideo0.Levels.GetValue(2)).ToString("f1") + "%";

            lblWidthV0.Text = ((Single)doVideo0.ProfileWidth.GetValue(0)).ToString("f2");
            lblWidthV1.Text = ((Single)doVideo0.ProfileWidth.GetValue(1)).ToString("f2");
            lblWidthV2.Text = ((Single)doVideo0.ProfileWidth.GetValue(2)).ToString("f2");
            lblWidthGaussV0.Text = ((Single)doVideo0.GaussWidth.GetValue(0)).ToString("f2");
            lblWidthGaussV1.Text = ((Single)doVideo0.GaussWidth.GetValue(1)).ToString("f2");
            lblWidthGaussV2.Text = ((Single)doVideo0.GaussWidth.GetValue(2)).ToString("f2");
            lblWidthW0.Text = ((Single)doVideo0.ProfileWidth.GetValue(3)).ToString("f2");
            lblWidthW1.Text = ((Single)doVideo0.ProfileWidth.GetValue(4)).ToString("f2");
            lblWidthW2.Text = ((Single)doVideo0.ProfileWidth.GetValue(5)).ToString("f2");
            lblWidthGaussW0.Text = ((Single)doVideo0.GaussWidth.GetValue(3)).ToString("f2");
            lblWidthGaussW1.Text = ((Single)doVideo0.GaussWidth.GetValue(4)).ToString("f2");
            lblWidthGaussW2.Text = ((Single)doVideo0.GaussWidth.GetValue(5)).ToString("f2");
            lblGaussCorrelatV.Text = ((Single)doVideo0.GaussCorrelation.GetValue(0)).ToString("f2");
            lblGaussCorrelatW.Text = ((Single)doVideo0.GaussCorrelation.GetValue(1)).ToString("f2");

            if (doVideo0.EnablePowerBucket == true)
            {
                labelDiametrA.Text = doVideo0.BucketSizeA.ToString("f2");
                labelDiametrB.Text = doVideo0.BucketSizeB.ToString("f2");
            }
        }

        private void cmbShutter_SelectedIndexChanged(object sender, EventArgs e)
        {
            doVideo0.Shutter = doVideo0.ShutterTable[cmbShutter.SelectedIndex];
        }

        private void cmbGain_SelectedIndexChanged(object sender, EventArgs e)
        {
            doVideo0.GainIndex = (UInt16)cmbGain.SelectedIndex;
        }

        private void radioButtonBucketType_CheckedChanged(object sender, EventArgs e)
        {
            RadioButton rb = (RadioButton)sender;

            if (rb.Name.Contains("Circle"))
                doVideo0.PowerBucket = DOVideoWCL.DOVideo.BucketType.eCircle;
            else if (rb.Name.Contains("Ellipse"))
                doVideo0.PowerBucket = DOVideoWCL.DOVideo.BucketType.eEllipse;
            else if (rb.Name.Contains("Rectangle"))
                doVideo0.PowerBucket = DOVideoWCL.DOVideo.BucketType.eRect;
        }

        private void numericUpDownEnergy_ValueChanged(object sender, EventArgs e)
        {
            doVideo0.BucketEnergy = Convert.ToSingle(numericUpDownEnergy.Value);
        }

        private void checkBoxPowerBucket_CheckedChanged(object sender, EventArgs e)
        {
            doVideo0.EnablePowerBucket = checkBoxPowerBucket.Checked;
            groupBoxBucketSize.Enabled = checkBoxPowerBucket.Checked;
            groupBoxEnergy.Enabled = checkBoxPowerBucket.Checked;
            gbBucketType.Enabled = checkBoxPowerBucket.Checked;
        }
    }
}