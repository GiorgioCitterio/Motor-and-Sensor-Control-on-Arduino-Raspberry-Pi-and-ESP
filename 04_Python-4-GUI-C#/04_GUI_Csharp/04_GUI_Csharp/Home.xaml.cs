namespace _04_GUI_Csharp;

public partial class Home : ContentPage
{
	public Home()
	{
		InitializeComponent();
	}

    private async void Sensore(object sender, EventArgs e)
    {
        await Navigation.PushAsync(new MenuSensore());
    }

    private async void Attuatore(object sender, EventArgs e)
    {
        await Navigation.PushAsync(new MenuAttuatore());
    }
}