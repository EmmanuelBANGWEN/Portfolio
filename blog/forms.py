from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, label='Nom')
#     email = forms.EmailField(label='Email')
#     formation = forms.ChoiceField(
#         choices=[
#             ('python', 'Deviens un développeur Python'),
#             ('productivite', 'Booster votre productivité'),
#             ('ia-aliment', "Formulation rapide d'aliments adaptés"),
#         ],
#         label='Formation',
#     )


from django import forms
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    email = forms.EmailField(label="Adresse Email")
    number = forms.CharField(label="Number")
    message = forms.CharField(widget=forms.Textarea, label="Message")

class ContactFormu(forms.Form):
    email = forms.EmailField(label="Adresse Email")
   