using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace barbut
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            
            button2.Visible = false;
            
            label3.Text = "";
            label5.Text = "";
            label8.Text = "";
            label10.Text = "";
            label11.Text = "";
            label14.Text = "";
            
            pictureBox1.BackgroundImage = null;
            pictureBox2.BackgroundImage = null;
            pictureBox3.BackgroundImage = null;
            pictureBox4.BackgroundImage = null;
            
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox3.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox4.SizeMode = PictureBoxSizeMode.Zoom;
        }
        
        int a=0, b=0, x=0, y=0, n=0, m=0, v=0, w=0,k=0, q = 0;
        
        Random rnd = new Random();
        private void menuStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {}
        private void reseteazaScorToolStripMenuItem_Click(object sender, EventArgs e)
        {
            label3.Text = "";
            label5.Text = "";
            label8.Text = "";
            label10.Text = "";
            
            v = 0;
            label11.Text = "";
            
            w = 0;
            label14.Text = "";
           
            pictureBox1.Image = null;
            pictureBox2.Image = null;
            pictureBox3.Image = null;
            pictureBox4.Image = null;
            
            button1.Visible = true;
            button2.Visible = false;
           
            k = 0;
        }
        private void joaca10JocuriToolStripMenuItem_Click(object sender, EventArgs e)
        {
            int i = 1;
            
            while (i <= 10)
            {
                button1.PerformClick();
                button2.PerformClick();
                i++;
            }
        }
        private void joaca100JocuriToolStripMenuItem_Click(object sender, EventArgs e)
        {
            int i = 1;
            
            while (i <= 100)
            {
                button1.PerformClick();
                button2.PerformClick();
                i++;
            }
        }
        private void arataReguliToolStripMenuItem_Click(object sender, EventArgs e)
        {
            q++;
           
            if (q % 2 == 1) label1.Visible = false;
            else label1.Visible = true;
        }
        private void button1_Click(object sender, EventArgs e)
         {
            a = rnd.Next(1, 7);
            b = rnd.Next(1, 7);
            label3.Text = a + ", " + b;
            label5.Text = "";
            
            m = a + b;
           
            button1.Visible = false;
            button2.Visible = true;
           
            if (a == 1) { pictureBox1.Image = Image.FromFile(@"1.png"); }
            else if (a == 2) { pictureBox1.Image = Image.FromFile(@"2.png"); }
            else if (a == 3) { pictureBox1.Image = Image.FromFile(@"3.png"); }
            else if (a == 4) { pictureBox1.Image = Image.FromFile(@"4.png"); }
            else if (a == 5) { pictureBox1.Image = Image.FromFile(@"5.png"); }
            else { pictureBox1.Image = Image.FromFile(@"6.png"); }
            
            if (b == 1) { pictureBox2.Image = Image.FromFile(@"1.png"); }
            else if (b == 2) { pictureBox2.Image = Image.FromFile(@"2.png"); }
            else if (b == 3) { pictureBox2.Image = Image.FromFile(@"3.png"); }
            else if (b == 4) { pictureBox2.Image = Image.FromFile(@"4.png"); }
            else if (b == 5) { pictureBox2.Image = Image.FromFile(@"5.png"); }
            else { pictureBox2.Image = Image.FromFile(@"6.png"); }
            
            pictureBox1.Refresh();
        }
        private void button2_Click(object sender, EventArgs e)
        {
            x = rnd.Next(1, 7);
            y = rnd.Next(1, 7);
            label5.Text = x + ", " + y;
            
            n = x + y;
            
            if (x == 1) { pictureBox3.Image = Image.FromFile(@"1.png"); }
            else if (x == 2) { pictureBox3.Image = Image.FromFile(@"2.png"); }
            else if (x == 3) { pictureBox3.Image = Image.FromFile(@"3.png"); }
            else if (x == 4) { pictureBox3.Image = Image.FromFile(@"4.png"); }
            else if (x == 5) { pictureBox3.Image = Image.FromFile(@"5.png"); }
            else { pictureBox3.Image = Image.FromFile(@"6.png"); }
            
            if (y == 1) { pictureBox4.Image = Image.FromFile(@"1.png"); }
            else if (y == 2) { pictureBox4.Image = Image.FromFile(@"2.png"); }
            else if (y == 3) { pictureBox4.Image = Image.FromFile(@"3.png"); }
            else if (y == 4) { pictureBox4.Image = Image.FromFile(@"4.png"); }
            else if (y == 5) { pictureBox4.Image = Image.FromFile(@"5.png"); }
            else { pictureBox4.Image = Image.FromFile(@"6.png"); }
           
            if (a == b && x != y) 
                { 
                    label8.Text = "Jucatorul1";
                    v = v + 1;
                    label10.Text = "";
                    label10.Text = v.ToString();
                }
            else if (a != b && x == y) 
                { 
                    label8.Text = "Jucatorul2";
                    w = w + 1;
                    label11.Text = "";
                    label11.Text = w.ToString(); 
                }
            else if (a == b && x == y && m > n) 
                { 
                    label8.Text = "Jucatorul1";
                    v = v + 1;
                    label10.Text = "";
                    label10.Text = v.ToString(); 
                }
            else if (a == b && x == y && m < n) 
                { 
                    label8.Text = "Jucatorul2";
                    w = w + 1;
                    label11.Text = "";
                    label11.Text = w.ToString();
                }
            else if (m == n) 
                { 
                    label8.Text = "Egal mai dati odata";
                    k = k + 1; 
                    label14.Text = "";
                    label14.Text = k.ToString();
                }
            else if (m <= 6 && m < n) 
                { 
                    label8.Text = "Jucatorul1";
                    v = v + 1;
                    label10.Text = "";
                    label10.Text = v.ToString();
                }
            else if (m <= 6 && m > n) 
                { 
                    label8.Text = "Jucatorul2";
                    w = w + 1;
                    label11.Text = "";
                    label11.Text = w.ToString();
                }
            else if (m >= 7 && m > n) 
                { 
                    label8.Text = "Jucatorul1";
                    v = v + 1;
                    label10.Text = ""; 
                    label10.Text = v.ToString(); 
                }
            else if (m >= 7 && m < n) 
                { 
                    label8.Text = "Jucatorul2";
                    w = w + 1;
                    label11.Text = ""; 
                    label11.Text = w.ToString(); 
                }
           
            button2.Visible = false;
            button1.Visible = true;
        }
    }
}
