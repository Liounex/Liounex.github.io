from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre Completo')
    email = forms.EmailField(label='Correo Electronico')
    message = forms.CharField(label='Ingrese su Mensaje', widget=forms.Textarea(attrs={'rows':4 }))