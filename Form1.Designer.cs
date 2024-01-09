namespace LorAI
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            downloader_page = new Panel();
            give_me_a_link = new Label();
            linkBox = new TextBox();
            download = new Button();
            Home = new ToolStripMenuItem();
            Managers = new ToolStripMenuItem();
            toolStripMenuItem2 = new ToolStripMenuItem();
            toolStripMenuItem3 = new ToolStripMenuItem();
            toolStripMenuItem4 = new ToolStripMenuItem();
            Downloader = new ToolStripMenuItem();
            Command_Handler = new ToolStripMenuItem();
            Explorer = new ToolStripMenuItem();
            Computer_Settings = new ToolStripMenuItem();
            dNSChangerToolStripMenuItem = new ToolStripMenuItem();
            clearTeToolStripMenuItem = new ToolStripMenuItem();
            performanceUpdaterToolStripMenuItem = new ToolStripMenuItem();
            Lorai_Settings = new ToolStripMenuItem();
            voiceEngineToolStripMenuItem = new ToolStripMenuItem();
            Addons = new ToolStripMenuItem();
            addonsForSocialMediaToolStripMenuItem = new ToolStripMenuItem();
            ınstagramRPCToolStripMenuItem = new ToolStripMenuItem();
            discordCustomRPCToolStripMenuItem = new ToolStripMenuItem();
            discordSelfBotToolStripMenuItem = new ToolStripMenuItem();
            Menu = new MenuStrip();
            downloader_page.SuspendLayout();
            Menu.SuspendLayout();
            SuspendLayout();
            // 
            // downloader_page
            // 
            downloader_page.BackColor = Color.Black;
            downloader_page.BackgroundImage = (Image)resources.GetObject("downloader_page.BackgroundImage");
            downloader_page.BackgroundImageLayout = ImageLayout.Stretch;
            downloader_page.Controls.Add(give_me_a_link);
            downloader_page.Controls.Add(linkBox);
            downloader_page.Controls.Add(download);
            downloader_page.Location = new Point(0, 25);
            downloader_page.Name = "downloader_page";
            downloader_page.Size = new Size(842, 426);
            downloader_page.TabIndex = 3;
            // 
            // give_me_a_link
            // 
            give_me_a_link.AutoSize = true;
            give_me_a_link.BackColor = Color.Transparent;
            give_me_a_link.Font = new Font("Segoe UI", 15.75F, FontStyle.Regular, GraphicsUnit.Point, 162);
            give_me_a_link.ForeColor = Color.White;
            give_me_a_link.Location = new Point(343, 22);
            give_me_a_link.Name = "give_me_a_link";
            give_me_a_link.Size = new Size(154, 30);
            give_me_a_link.TabIndex = 3;
            give_me_a_link.Text = "Give me a link :";
            // 
            // linkBox
            // 
            linkBox.Location = new Point(237, 69);
            linkBox.Name = "linkBox";
            linkBox.Size = new Size(357, 23);
            linkBox.TabIndex = 2;
            // 
            // download
            // 
            download.BackColor = Color.PaleVioletRed;
            download.BackgroundImageLayout = ImageLayout.None;
            download.Cursor = Cursors.Hand;
            download.FlatAppearance.BorderSize = 0;
            download.FlatStyle = FlatStyle.Popup;
            download.ForeColor = Color.FromArgb(192, 0, 192);
            download.Location = new Point(360, 98);
            download.Name = "download";
            download.Size = new Size(104, 24);
            download.TabIndex = 1;
            download.Text = "Download";
            download.UseVisualStyleBackColor = false;
            download.Click += button1_Click;
            // 
            // Home
            // 
            Home.Name = "Home";
            Home.Size = new Size(52, 20);
            Home.Text = "Home";
            Home.Click += homeToolStripMenuItem_Click;
            // 
            // Managers
            // 
            Managers.DropDownItems.AddRange(new ToolStripItem[] { toolStripMenuItem2, toolStripMenuItem3, toolStripMenuItem4 });
            Managers.Name = "Managers";
            Managers.Size = new Size(71, 20);
            Managers.Text = "Managers";
            Managers.Click += Managers_Click;
            // 
            // toolStripMenuItem2
            // 
            toolStripMenuItem2.Name = "toolStripMenuItem2";
            toolStripMenuItem2.Size = new Size(184, 22);
            toolStripMenuItem2.Text = "Credit Card Manager";
            toolStripMenuItem2.Click += toolStripMenuItem2_Click;
            // 
            // toolStripMenuItem3
            // 
            toolStripMenuItem3.Name = "toolStripMenuItem3";
            toolStripMenuItem3.Size = new Size(184, 22);
            toolStripMenuItem3.Text = "Shortcut Manager";
            // 
            // toolStripMenuItem4
            // 
            toolStripMenuItem4.Name = "toolStripMenuItem4";
            toolStripMenuItem4.Size = new Size(184, 22);
            toolStripMenuItem4.Text = "Password Manager";
            // 
            // Downloader
            // 
            Downloader.Name = "Downloader";
            Downloader.Size = new Size(83, 20);
            Downloader.Text = "Downloader";
            Downloader.Click += downloaderToolStripMenuItem_Click;
            // 
            // Command_Handler
            // 
            Command_Handler.Name = "Command_Handler";
            Command_Handler.Size = new Size(121, 20);
            Command_Handler.Text = "Command Handler";
            Command_Handler.Click += commandHandlerToolStripMenuItem_Click;
            // 
            // Explorer
            // 
            Explorer.Name = "Explorer";
            Explorer.Size = new Size(62, 20);
            Explorer.Text = "Explorer";
            Explorer.Click += Explorer_Click;
            // 
            // Computer_Settings
            // 
            Computer_Settings.DropDownItems.AddRange(new ToolStripItem[] { dNSChangerToolStripMenuItem, clearTeToolStripMenuItem, performanceUpdaterToolStripMenuItem });
            Computer_Settings.Name = "Computer_Settings";
            Computer_Settings.Size = new Size(118, 20);
            Computer_Settings.Text = "Computer Settings";
            Computer_Settings.Click += Computer_Settings_Click;
            // 
            // dNSChangerToolStripMenuItem
            // 
            dNSChangerToolStripMenuItem.Name = "dNSChangerToolStripMenuItem";
            dNSChangerToolStripMenuItem.Size = new Size(187, 22);
            dNSChangerToolStripMenuItem.Text = "DNS Changer";
            // 
            // clearTeToolStripMenuItem
            // 
            clearTeToolStripMenuItem.Name = "clearTeToolStripMenuItem";
            clearTeToolStripMenuItem.Size = new Size(187, 22);
            clearTeToolStripMenuItem.Text = "Clear Temp";
            // 
            // performanceUpdaterToolStripMenuItem
            // 
            performanceUpdaterToolStripMenuItem.Name = "performanceUpdaterToolStripMenuItem";
            performanceUpdaterToolStripMenuItem.Size = new Size(187, 22);
            performanceUpdaterToolStripMenuItem.Text = "Performance Updater";
            // 
            // Lorai_Settings
            // 
            Lorai_Settings.DropDownItems.AddRange(new ToolStripItem[] { voiceEngineToolStripMenuItem });
            Lorai_Settings.Name = "Lorai_Settings";
            Lorai_Settings.Size = new Size(92, 20);
            Lorai_Settings.Text = "LorAI Settings";
            Lorai_Settings.Click += Lorai_Settings_Click;
            // 
            // voiceEngineToolStripMenuItem
            // 
            voiceEngineToolStripMenuItem.Name = "voiceEngineToolStripMenuItem";
            voiceEngineToolStripMenuItem.Size = new Size(141, 22);
            voiceEngineToolStripMenuItem.Text = "Voice Engine";
            // 
            // Addons
            // 
            Addons.DropDownItems.AddRange(new ToolStripItem[] { addonsForSocialMediaToolStripMenuItem });
            Addons.Name = "Addons";
            Addons.Size = new Size(60, 20);
            Addons.Text = "Addons";
            Addons.Click += Addons_Click;
            // 
            // addonsForSocialMediaToolStripMenuItem
            // 
            addonsForSocialMediaToolStripMenuItem.DropDownItems.AddRange(new ToolStripItem[] { ınstagramRPCToolStripMenuItem, discordCustomRPCToolStripMenuItem, discordSelfBotToolStripMenuItem });
            addonsForSocialMediaToolStripMenuItem.Name = "addonsForSocialMediaToolStripMenuItem";
            addonsForSocialMediaToolStripMenuItem.Size = new Size(202, 22);
            addonsForSocialMediaToolStripMenuItem.Text = "Addons for social media";
            // 
            // ınstagramRPCToolStripMenuItem
            // 
            ınstagramRPCToolStripMenuItem.Name = "ınstagramRPCToolStripMenuItem";
            ınstagramRPCToolStripMenuItem.Size = new Size(184, 22);
            ınstagramRPCToolStripMenuItem.Text = "Instagram RPC";
            ınstagramRPCToolStripMenuItem.Click += ınstagramRPCToolStripMenuItem_Click;
            // 
            // discordCustomRPCToolStripMenuItem
            // 
            discordCustomRPCToolStripMenuItem.Name = "discordCustomRPCToolStripMenuItem";
            discordCustomRPCToolStripMenuItem.Size = new Size(184, 22);
            discordCustomRPCToolStripMenuItem.Text = "Discord Custom RPC";
            // 
            // discordSelfBotToolStripMenuItem
            // 
            discordSelfBotToolStripMenuItem.Name = "discordSelfBotToolStripMenuItem";
            discordSelfBotToolStripMenuItem.Size = new Size(184, 22);
            discordSelfBotToolStripMenuItem.Text = "Discord Self Bot";
            // 
            // Menu
            // 
            Menu.Items.AddRange(new ToolStripItem[] { Home, Managers, Downloader, Command_Handler, Explorer, Computer_Settings, Lorai_Settings, Addons });
            Menu.Location = new Point(0, 0);
            Menu.Name = "Menu";
            Menu.Size = new Size(842, 24);
            Menu.TabIndex = 1;
            Menu.Text = "menuStrip1";
            Menu.ItemClicked += Menu_ItemClicked;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.MenuHighlight;
            ClientSize = new Size(842, 449);
            Controls.Add(Menu);
            Controls.Add(downloader_page);
            FormBorderStyle = FormBorderStyle.Fixed3D;
            MainMenuStrip = Menu;
            MaximizeBox = false;
            Name = "Form1";
            RightToLeft = RightToLeft.No;
            Text = "LorAI";
            Load += Form1_Load;
            downloader_page.ResumeLayout(false);
            downloader_page.PerformLayout();
            Menu.ResumeLayout(false);
            Menu.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion
        private Panel downloader_page;
        private Button download;
        private TextBox linkBox;
        private Label give_me_a_link;
        private ToolStripMenuItem Home;
        private ToolStripMenuItem Managers;
        private ToolStripMenuItem toolStripMenuItem2;
        private ToolStripMenuItem toolStripMenuItem3;
        private ToolStripMenuItem toolStripMenuItem4;
        private ToolStripMenuItem Downloader;
        private ToolStripMenuItem Command_Handler;
        private ToolStripMenuItem Explorer;
        private ToolStripMenuItem Computer_Settings;
        private ToolStripMenuItem dNSChangerToolStripMenuItem;
        private ToolStripMenuItem clearTeToolStripMenuItem;
        private ToolStripMenuItem performanceUpdaterToolStripMenuItem;
        private ToolStripMenuItem Lorai_Settings;
        private ToolStripMenuItem voiceEngineToolStripMenuItem;
        private ToolStripMenuItem Addons;
        private ToolStripMenuItem addonsForSocialMediaToolStripMenuItem;
        private ToolStripMenuItem ınstagramRPCToolStripMenuItem;
        private ToolStripMenuItem discordCustomRPCToolStripMenuItem;
        private ToolStripMenuItem discordSelfBotToolStripMenuItem;
        private MenuStrip Menu;
    }
}
