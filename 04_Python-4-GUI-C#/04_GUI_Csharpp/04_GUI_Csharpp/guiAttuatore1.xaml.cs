using System.IO.Ports;
namespace _04_GUI_Csharpp;

public struct Pack
{
    public const string IDCORRETTO = "BE";
    public const string MITTENTE = "M001";
    public const string DESTINATARIO = "D031";
    public const string TIPO = "A1";
    public string direzione = "A";
    public int velocita = 0;
    public const string VUOTO = "----------------";

    public Pack()
    {
    }
}
public partial class guiAttuatore1 : ContentPage
{
    static SerialPort serialPort = new SerialPort("COM3", 9600);
    
    public guiAttuatore1()
    {
        InitializeComponent();
    }
    private void Inc10(object sender, EventArgs e)
    {
        //pack.velocita += 10;
        //if (pack.velocita >= 250)
        //    pack.velocita = 250;
        //else
        //    pack.velocita += 10;
        //Velocità.Text = "Velocità: " + pack.velocita.ToString();
        //serialPort.Open();
        //serialPort.Write(pack);
        //serialPort.Close();
        //Console.WriteLine(pack);
    }

    private void Dec10(object sender, EventArgs e)
    {
        //pack.velocita -= 10;
        //if (pack.velocita >= 250)
        //    pack.velocita = 250;
        //else
        //    pack.velocita -= 10;
        //Velocità.Text = "Velocità: " + pack.velocita.ToString();
        //serialPort.Open();
        //serialPort.Write(pack);
        //serialPort.Close();
        //Console.WriteLine(pack);
    }

    private void Avanti(object sender, EventArgs e)
    {

    }

    private void Indietro(object sender, EventArgs e)
    {

    }
}