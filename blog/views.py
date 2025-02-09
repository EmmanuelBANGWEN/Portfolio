import json
from django.shortcuts import render
from django.templatetags.static import static
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact 
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm, ContactFormu
from django.conf import settings
from .models import Contact

# def homeblog(request):
#     return render(request, 'blog.html')


# def homeblog(request):
#     # Charger le fichier JSON
#     json_file = static("blog/articles.json")  # Chemin du fichier JSON
#     with open(json_file, encoding="utf-8") as file:
#         articles = json.load(file)

#     return render(request, "blog.html", {"articles": articles})

import os
import json
from django.conf import settings

def homeblog(request):
    # Obtenir le chemin complet du fichier JSON
    json_file = os.path.join(settings.BASE_DIR, "static", "blog", "articles.json")

    # Charger le fichier JSON
    try:
        with open(json_file, encoding="utf-8") as file:
            articles = json.load(file)
    except FileNotFoundError:
        articles = []  # Si le fichier n'est pas trouvé, retourner une liste vide
    except json.JSONDecodeError as e:
        print("Erreur de décodage JSON :", e)
        articles = []


    return render(request, "blog.html", {"articles": articles})



def about(request):
    return render(request, 'about.html')

def formations(request):
    return render(request, 'formations.html')

def contact(request):
    return render(request, 'contact.html')

def aliments(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            # Récupération des données
            # name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # number = form.cleaned_data['number']
            # message = form.cleaned_data['message']

            # Enregistrement en base de données
            Contact.objects.create(
                # name=name,
                email=email,
                # number=number,
                # message=message
            )

            # Envoi de l'email
            send_mail(
                subject=f"Nouveau message de {email} Venu du site web emmanuelbangwen.com pour le guide aliment de precision",
                message=f"Venu du site web emmanuelbangwen.com pour le guide gratuit aliment de precision : ({email})",
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('aliments')  # Redirection pour éviter les resoumissions
    else:
        form = ContactForm()
    return render(request, 'aliments.html')

def python(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            # Récupération des données
            # name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # number = form.cleaned_data['number']
            # message = form.cleaned_data['message']

            # Enregistrement en base de données
            Contact.objects.create(
                # name=name,
                email=email,
                # number=number,
                # message=message
            )

            # Envoi de l'email
            send_mail(
                subject=f"Nouveau message de {email} Venu du site web emmanuelbangwen.com pour le guide gratuit python",
                message=f"Venu du site web emmanuelbangwen.com pour le guide gratuit python : ({email})",
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('python')  # Redirection pour éviter les resoumissions
    else:
        form = ContactForm()
    return render(request, 'python.html')

# def booster(request):
    
def booster(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Récupération des données
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            message = form.cleaned_data['message']

            # Enregistrement en base de données
            Contact.objects.create(
                name=name,
                email=email,
                number=number,
                message=message
            )

            # Envoi de l'email
            send_mail(
                subject=f"Nouveau message de {email} Venu du site web emmanuelbangwen.com le guide gratuit sur l'Intelligence Artificielle",
                message=f"Venu du site web emmanuelbangwen.com pour le guide l'Intelligence Artificielle : ({email})",
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('booster')  # Redirection pour éviter les resoumissions
    else:
        form = ContactForm()

    return render(request, 'booster.html', {'form': form})

    # return render(request, 'booster.html')

# def final_aliment(request):
#     return render(request, 'final_aliment.html')


def final_aliment(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Récupération des données
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            message = form.cleaned_data['message']

            # Enregistrement en base de données
            Contact.objects.create(
                name=name,
                email=email,
                number=number,
                message=message
            )

            # Envoi de l'email
            send_mail(
                subject=f"Nouveau message de {email} Venu du site web emmanuelbangwen.com  pour payer la formation de precision",
                message=f"Venu du site web emmanuelbangwen.com pour payer la formation aliment de precision : ({email})",
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )


            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('final_aliment')  # Redirection pour éviter les resoumissions
    else:
        form = ContactForm()

    return render(request, 'final_aliment.html', {'form': form})

    # return render(request, 'inscription.html')  # Crée ce fichier dans templates/


def final_python(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Récupération des données
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            message = form.cleaned_data['message']

            # Enregistrement en base de données
            Contact.objects.create(
                name=name,
                email=email,
                number=number,
                message=message
            )

            # Envoi de l'email
            send_mail(
                subject=f"Nouveau message de {email} Venu du site web emmanuelbangwen.com pour payer la formation python",
                message=f"Venu du site web emmanuelbangwen.com pour payer la formation python : ({email})",
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )


            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('final_python')  # Redirection pour éviter les resoumissions
    else:
        form = ContactForm()

    return render(request, 'final_python.html', {'form': form})

    # return render(request, 'inscription.html')  # Crée ce fichier dans templates/




def final_booster(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Récupération des données
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            message = form.cleaned_data['message']

            # Enregistrement en base de données
            Contact.objects.create(
                name=name,
                email=email,
                number=number,
                message=message
            )

            # Envoi de l'email
            send_mail(
                subject=f"Nouveau message de {email} Venu du site web emmanuelbangwen.com pour payer la formation sur l'Intelligence Artificielle",
                message=f"Venu du site web emmanuelbangwen.com pour le guide aliment de precision l'Intelligence Artificielle : ({email})",
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('final_booster')  # Redirection pour éviter les resoumissions
    else:
        form = ContactForm()

    return render(request, 'final_booster.html', {'form': form})

    # return render(request, 'inscription.html')  # Crée ce fichier dans templates/



# def tarifs(request):
#     return render(request, 'tarifs.html')


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm  # Si vous avez un formulaire Django personnalisé
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extraction des données du formulaire
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            formation = form.cleaned_data['formation']
            
            # Envoi d'email
            try:
                send_mail(
                    subject=f"Message de : {name}",
                    message=f"Formation choisie : {formation}\nEmail : {email}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['bikoyemmanuel531@gmail.com'],  # Changez par votre email
                )
                messages.success(request, 'Votre message a été envoyé avec succès!')
            except Exception as e:
                messages.error(request, "Une erreur est survenue lors de l'envoi de votre message.")
                print(e)
            return redirect('contact_view')
        else:
            messages.error(request, 'Veuillez remplir le formulaire correctement.')
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form})


import os
import json
from django.shortcuts import render, get_object_or_404
from django.conf import settings

def blog_details(request, article_id):
    # Charger les articles
    # json_file = os.path.join(settings.BASE_DIR, "portfolio", "static", "blog", "articles.json")
    json_file = os.path.join(settings.BASE_DIR, "static", "blog", "articles.json")

    try:
        with open(json_file, encoding="utf-8") as file:
            articles = json.load(file)
            
    except FileNotFoundError:
        articles = []
    
    # Trouver l'article par son ID
    article = next((a for a in articles if a["id"] == article_id), None)

    if not article:
        return render(request, "404.html", {"message": "Article introuvable"})  # Gérer l'erreur si l'article n'existe pas
    
    return render(request, "blog_details.html", {"article": article})
