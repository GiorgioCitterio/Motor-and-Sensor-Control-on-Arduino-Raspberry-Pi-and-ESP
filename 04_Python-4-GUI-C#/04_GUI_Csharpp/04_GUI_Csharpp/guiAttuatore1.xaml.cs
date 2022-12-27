using System.IO.Ports;
using System.Runtime.InteropServices;
namespace _04_GUI_Csharpp;

[StructLayout(LayoutKind.Explicit)]
public struct pack
{
    [FieldOffset(0)]
    public byte IDCORRETTO = "BE";
    [FieldOffset(1)]
    public byte MITTENTE = "M001";
    [FieldOffset(5)]
    public byte DESTINATARIO = "D031";
    [FieldOffset(9)]
    public byte TIPO = "A1";
    [FieldOffset(11)]
    public byte direzione = "A";
    [FieldOffset(12)]
    public byte velocita = 0;
    [FieldOffset(15)]
    public byte VUOTO = "----------------";
}
public partial class guiAttuatore1 : ContentPage
{
	static SerialPort serialPort = new SerialPort("COM3", 9600);   
	public guiAttuatore1()
	{
		InitializeComponent();
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