import json
from django.shortcuts import render
from django.templatetags.static import static

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

# def blog_details(request):
#     return render(request, 'blog_details.html')


def tarifs(request):
    return render(request, 'tarifs.html')


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

    return render(request, 'tarifs.html', {'form': form})


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
