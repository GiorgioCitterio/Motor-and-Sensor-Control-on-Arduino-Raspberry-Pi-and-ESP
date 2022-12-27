namespace _04_GUI_Csharpp;

public partial class App : Application
{
	public App()
	{
		InitializeComponent();

		MainPage = new NavigationPage(new Home());
	}
}
