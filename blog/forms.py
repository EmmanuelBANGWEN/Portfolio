from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nom')
    email = forms.EmailField(label='Email')
    formation = forms.ChoiceField(
        choices=[
            ('python', 'Deviens un développeur Python'),
            ('productivite', 'Booster votre productivité'),
            ('ia-aliment', "Formulation rapide d'aliments adaptés"),
        ],
        label='Formation',
    )
