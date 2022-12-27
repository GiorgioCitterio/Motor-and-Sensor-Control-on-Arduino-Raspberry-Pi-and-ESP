using System.IO.Ports;
namespace _04_GUI_Csharpp;

public partial class guiAttuatore1 : ContentPage
{
	static SerialPort serialPort;
	public guiAttuatore1()
	{
		InitializeComponent();
	}
}