using System.IO.Ports;
using System.Text.Encodings;
namespace _04_GUI_Csharpp;

[StructLayout(LayoutKind.Explicit)]
public struct Pack
{
    
}
public partial class guiAttuatore1 : ContentPage
{
	static SerialPort serialPort = new SerialPort("COM3", 9600);
    static const byte[] IDCORRETTO = Encoding.ASCII.GetBytes("BE");
    static const byte[] MITTENTE =  "M001";
    static const string DESTINATARIO = "D031";
    static const string TIPO = "A1";
    static byte direzione = "A";
    static byte velocita = 0;
    static const string VUOTO = "----------------";
    public guiAttuatore1()
	{
		InitializeComponent();
        Pack pack = new Pack();
	}
    private void Inc10(object sender, EventArgs e)
    {
        pack.velocita += 10;
        if (pack.velocita >= 250)
            pack.velocita = 250;
        else
            pack.velocita += 10;
        Velocità.Text= "Velocità: "+pack.velocita.ToString();
        serialPort.Open();
        serialPort.Write(pack);
        serialPort.Close();
        Console.WriteLine(pack);
    }

    private void Dec10(object sender, EventArgs e)
    {
        pack.velocita -= 10;
        if (pack.velocita >= 250)
            pack.velocita = 250;
        else
            pack.velocita -= 10;
        Velocità.Text = "Velocità: " + pack.velocita.ToString();
        serialPort.Open();
        serialPort.Write(pack);
        serialPort.Close();
        Console.WriteLine(pack);
    }

    private void Avanti(object sender, EventArgs e)
    {
        
    }

    private void Indietro(object sender, EventArgs e)
    {

    }
}