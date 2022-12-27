namespace _04_GUI_Csharpp;

public partial class MenuAttuatore : ContentPage
{
	public MenuAttuatore()
	{
		InitializeComponent();
	}
    private async void Soluzione1(object sender, EventArgs e)
    {
        await Navigation.PushAsync(new guiAttuatore1());
    }

    private async void Soluzione2(object sender, EventArgs e)
    {
        await Navigation.PushAsync(new guiAttuatore2());
    }

    private async void Soluzione3(object sender, EventArgs e)
    {
        await Navigation.PushAsync(new guiAttuatore3());
    }
}