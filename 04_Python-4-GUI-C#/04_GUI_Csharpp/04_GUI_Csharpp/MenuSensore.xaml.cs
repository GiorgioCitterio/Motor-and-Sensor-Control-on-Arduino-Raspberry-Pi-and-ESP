namespace _04_GUI_Csharpp;

public partial class MenuSensore : ContentPage
{
	public MenuSensore()
	{
		InitializeComponent();
	}
    private async void Soluzione1(object sender, EventArgs e)
    {
        await Navigation.PushAsync(new guiSensore1());
    }

    private async void Soluzione2(object sender, EventArgs e)
    {
        await Navigation.PushAsync(new guiSensore2());
    }

    private async void Soluzione3(object sender, EventArgs e)
    {
        await Navigation.PushAsync(new guiSensore3());
    }
}