from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(label="Name", max_length=250)
    address = forms.CharField(label="Address", max_length=250)
    mob_no = forms.CharField(label="Mob", max_length=250)


class AForm(forms.Form):
    name = forms.CharField(label="Name", max_length=250)

