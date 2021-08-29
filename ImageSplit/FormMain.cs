using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ImageSplit
{
    public partial class FormMain : Form
    {
        readonly string[] imgExt =
        {
            "png",
            "PNG",
            "jpg",
            "JPG",
            "bmp",
            "BMP"
        };

        private List<string> convertFileList;

        /// <summary>
        /// メインフォーム コンストラクタ
        /// </summary>
        public FormMain()
        {
            // フォーム初期化
            InitializeComponent();

            // インスタンス初期化
            convertFileList = new List<string>();
        }

        /// <summary>
        /// ドラッグドロップ時処理
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void FormMain_DragDrop(object sender, DragEventArgs e)
        {
            // ドロップファイルのパスリスト
            string[] files = (string[])e.Data.GetData(DataFormats.FileDrop, false);

            textBoxLog.Clear();
            convertFileList.Clear();
            textBoxLog.AppendText("ドロップファイル");
            foreach (string file in files)
            {
                textBoxLog.AppendText(file + Environment.NewLine);

                // 拡張子チェック
                string[] ext = file.Split('.');
                foreach (string check in imgExt)
                {
                    if (ext[ext.Count() - 1] == check)
                    {
                        convertFileList.Add(file);
                        break;
                    }
                }

            }
        }

        /// <summary>
        /// メインフォームでのドラッグ時処理
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void FormMain_DragEnter(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.FileDrop))
            {
                e.Effect = DragDropEffects.All;
            }
            else
            {
                e.Effect = DragDropEffects.None;
            }
        }

        /// <summary>
        /// 「開く」ボタンクリック時処理
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void buttonFileOpen_Click(object sender, EventArgs e)
        {

        }

        /// <summary>
        /// 「変換」ボタンクリック時処理
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void buttonConverter_Click(object sender, EventArgs e)
        {
            int splitWidth = (int)numericUpDownWidth.Value;
            int splitHeight = (int)numericUpDownHeight.Value;

            textBoxLog.AppendText("変換ファイル" + Environment.NewLine);
            foreach (string file in convertFileList)
            {
                textBoxLog.AppendText(file + Environment.NewLine);

                // 画像を指定して読み込み
                Bitmap bmp = new Bitmap(Image.FromFile(file));

                // 画像が指定サイズで分割できるか確認
                if (bmp.Width % splitWidth == 0 && bmp.Height % splitHeight == 0)
                {
                    string saveFile;
                    Rectangle rect;
                    Bitmap splitBmp;

                    for(int x = 0; x < bmp.Width / splitWidth; x++)
                    {
                        for(int y = 0; y < bmp.Height / splitHeight; y++)
                        {
                            rect = new Rectangle(splitWidth * x, splitHeight * y, splitWidth, splitHeight);
                            splitBmp = bmp.Clone(rect, bmp.PixelFormat);
                            saveFile = file + "-" + x.ToString() + "-" + y.ToString() + ".PNG";
                            splitBmp.Save(saveFile, System.Drawing.Imaging.ImageFormat.Png);
                            textBoxLog.AppendText(saveFile + Environment.NewLine);
                        }
                    }
                }
                else
                {
                    textBoxLog.AppendText(file + "は指定したサイズで分割できません．");
                }
            }
        }

        private void textBoxLog_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
