from django import forms


class ReseñaForm(forms.Form):
    titulo = forms.CharField(required=True, max_length=64) 
    subtitulo = forms.CharField(required=True, max_length=64) 
    cuerpo = forms.CharField(required=True)
    autor = forms.CharField(max_length=64)
    fecha = forms.DateField()