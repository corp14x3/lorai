using Microsoft.VisualBasic.ApplicationServices;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.StartPanel;
namespace LorAI
{
    public partial class Form1 : Form
    {
        string userName = Environment.UserName;
        public Form1()
        {
            InitializeComponent();
        }
        private void homeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            home_page.Visible = true;
            downloader_page.Visible = false;
        }
        private void Managers_Click(object sender, EventArgs e)
        {

        }
        private void downloaderToolStripMenuItem_Click(object sender, EventArgs e)
        {
            downloader_page.Visible = true;
            home_page.Visible = false;
        }
        private void commandHandlerToolStripMenuItem_Click(object sender, EventArgs e)
        {
            downloader_page.Visible = false;
            home_page.Visible = false;
        }
        private void Explorer_Click(object sender, EventArgs e)
        {

        }
        private void Form1_Load(object sender, EventArgs e)
        {

        }
        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {

        }
        private void Computer_Settings_Click(object sender, EventArgs e)
        {

        }
        private void Lorai_Settings_Click(object sender, EventArgs e)
        {

        }
        private void Addons_Click(object sender, EventArgs e)
        {

        }
        private void button1_Click(object sender, EventArgs e)
        {
            string link = linkBox.Text;
            string arguments = $"{link}";
            string pythonScript = "C:\\Users\\corp1\\Desktop\\lorai\\commands\\loraid.py";
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo
            {
                FileName = $"C:\\Users\\{userName}\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
                Arguments = $"{pythonScript} {arguments}",
                RedirectStandardOutput = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };
            process.StartInfo = startInfo;
            process.Start();
        }
        private void ýnstagramRPCToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void Menu_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }
    }
}