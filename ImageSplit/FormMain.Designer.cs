
namespace ImageSplit
{
    partial class FormMain
    {
        /// <summary>
        /// 必要なデザイナー変数です。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 使用中のリソースをすべてクリーンアップします。
        /// </summary>
        /// <param name="disposing">マネージド リソースを破棄する場合は true を指定し、その他の場合は false を指定します。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows フォーム デザイナーで生成されたコード

        /// <summary>
        /// デザイナー サポートに必要なメソッドです。このメソッドの内容を
        /// コード エディターで変更しないでください。
        /// </summary>
        private void InitializeComponent()
        {
            this.numericUpDownWidth = new System.Windows.Forms.NumericUpDown();
            this.numericUpDownHeight = new System.Windows.Forms.NumericUpDown();
            this.labelTimes = new System.Windows.Forms.Label();
            this.labelRes = new System.Windows.Forms.Label();
            this.buttonFileOpen = new System.Windows.Forms.Button();
            this.buttonConverter = new System.Windows.Forms.Button();
            this.textBoxLog = new System.Windows.Forms.TextBox();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownWidth)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownHeight)).BeginInit();
            this.SuspendLayout();
            // 
            // numericUpDownWidth
            // 
            this.numericUpDownWidth.Location = new System.Drawing.Point(361, 51);
            this.numericUpDownWidth.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.numericUpDownWidth.Maximum = new decimal(new int[] {
            1920,
            0,
            0,
            0});
            this.numericUpDownWidth.Name = "numericUpDownWidth";
            this.numericUpDownWidth.Size = new System.Drawing.Size(115, 22);
            this.numericUpDownWidth.TabIndex = 0;
            this.numericUpDownWidth.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.numericUpDownWidth.Value = new decimal(new int[] {
            64,
            0,
            0,
            0});
            // 
            // numericUpDownHeight
            // 
            this.numericUpDownHeight.Location = new System.Drawing.Point(511, 51);
            this.numericUpDownHeight.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.numericUpDownHeight.Maximum = new decimal(new int[] {
            1920,
            0,
            0,
            0});
            this.numericUpDownHeight.Name = "numericUpDownHeight";
            this.numericUpDownHeight.Size = new System.Drawing.Size(115, 22);
            this.numericUpDownHeight.TabIndex = 1;
            this.numericUpDownHeight.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.numericUpDownHeight.Value = new decimal(new int[] {
            64,
            0,
            0,
            0});
            // 
            // labelTimes
            // 
            this.labelTimes.AutoSize = true;
            this.labelTimes.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F);
            this.labelTimes.Location = new System.Drawing.Point(484, 54);
            this.labelTimes.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.labelTimes.Name = "labelTimes";
            this.labelTimes.Size = new System.Drawing.Size(18, 18);
            this.labelTimes.TabIndex = 2;
            this.labelTimes.Text = "X";
            // 
            // labelRes
            // 
            this.labelRes.AutoSize = true;
            this.labelRes.Location = new System.Drawing.Point(299, 56);
            this.labelRes.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.labelRes.Name = "labelRes";
            this.labelRes.Size = new System.Drawing.Size(52, 15);
            this.labelRes.TabIndex = 3;
            this.labelRes.Text = "解像度";
            // 
            // buttonFileOpen
            // 
            this.buttonFileOpen.Location = new System.Drawing.Point(417, 15);
            this.buttonFileOpen.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.buttonFileOpen.Name = "buttonFileOpen";
            this.buttonFileOpen.Size = new System.Drawing.Size(100, 29);
            this.buttonFileOpen.TabIndex = 4;
            this.buttonFileOpen.Text = "開く";
            this.buttonFileOpen.UseVisualStyleBackColor = true;
            this.buttonFileOpen.Click += new System.EventHandler(this.buttonFileOpen_Click);
            // 
            // buttonConverter
            // 
            this.buttonConverter.Location = new System.Drawing.Point(525, 15);
            this.buttonConverter.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.buttonConverter.Name = "buttonConverter";
            this.buttonConverter.Size = new System.Drawing.Size(100, 29);
            this.buttonConverter.TabIndex = 5;
            this.buttonConverter.Text = "変換";
            this.buttonConverter.UseVisualStyleBackColor = true;
            this.buttonConverter.Click += new System.EventHandler(this.buttonConverter_Click);
            // 
            // textBoxLog
            // 
            this.textBoxLog.Location = new System.Drawing.Point(16, 82);
            this.textBoxLog.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.textBoxLog.Multiline = true;
            this.textBoxLog.Name = "textBoxLog";
            this.textBoxLog.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.textBoxLog.Size = new System.Drawing.Size(608, 464);
            this.textBoxLog.TabIndex = 6;
            this.textBoxLog.TextChanged += new System.EventHandler(this.textBoxLog_TextChanged);
            // 
            // FormMain
            // 
            this.AllowDrop = true;
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(640, 562);
            this.Controls.Add(this.textBoxLog);
            this.Controls.Add(this.buttonConverter);
            this.Controls.Add(this.buttonFileOpen);
            this.Controls.Add(this.labelRes);
            this.Controls.Add(this.labelTimes);
            this.Controls.Add(this.numericUpDownHeight);
            this.Controls.Add(this.numericUpDownWidth);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.Name = "FormMain";
            this.Text = "画像分割";
            this.DragDrop += new System.Windows.Forms.DragEventHandler(this.FormMain_DragDrop);
            this.DragEnter += new System.Windows.Forms.DragEventHandler(this.FormMain_DragEnter);
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownWidth)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownHeight)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.NumericUpDown numericUpDownWidth;
        private System.Windows.Forms.NumericUpDown numericUpDownHeight;
        private System.Windows.Forms.Label labelTimes;
        private System.Windows.Forms.Label labelRes;
        private System.Windows.Forms.Button buttonFileOpen;
        private System.Windows.Forms.Button buttonConverter;
        private System.Windows.Forms.TextBox textBoxLog;

    }
}

