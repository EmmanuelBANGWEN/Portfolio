from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact 
from .forms import ContactForm
from django.core.mail import send_mail


# from django.contrib.auth.decorators import login_required
# def home(request):
#     return render(request,'index.html')


# # @login_required(login_url='')
# def contact(request):
#    if request.method=="POST":
#        print('post')
#        name=request.POST.get('name')
#        email=request.POST.get('email')
#        number=request.POST.get('number')
#        content=request.POST.get('content')
#        print(name,email,number,content )

#        if len(name)>1 and len(name)<30:
#            pass
#        else:
#            messages.error(request,'Lenght of name should be greater than 2 and less than 30 words ')
#            return render(request,'home.html')
       
#        if len (email)>1 and len(email)<30:
#            pass
#        else:
#            messages.error(request,'invaild email try again ')
#            return render(request,'home.html')
#        print(len(number))
#        if  len(number)>9 and len(number)<13:
#            pass
#        else:
#            messages.error(request,'invaild number please try again ')
#            return render(request,'home.html')
#        ins = models.Contact(name=name,email=email,content=content,number=number)
#        ins.save()
#        messages.success(request,'Thank You for contacting me!! Your message has been saved ')
#        print('data has been saved to database')
 
#        print('The request is no pass ')
#    return render(request,'home.html')


def consultations(request):
    return render(request, 'consultations.html')

def developpement(request):
    return render(request, 'developpement.html')

def marketing(request):
    return render(request, 'marketing.html')

def business(request):
    return render(request, 'business.html')

def transformation(request):
    return render(request, 'transformation.html')

def bangri(request):
    return render(request, 'bangri.html')

def bangpig(request):
    return render(request, 'bangpig.html')

def zbang(request):
    return render(request, 'zbang.html')

def bangquiz(request):
    return render(request, 'bangquiz.html')

def optimisation(request):
    return render(request, 'optimisation.html')

def bigdata(request):
    return render(request, 'bigdata.html')

def nutrition(request):
    return render(request, 'nutrition.html')

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from .models import Contact  # Import du modèle Contact si tu l'utilises
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings
from .models import Contact

def home(request):
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
                subject=f"Nouveau message de {name}",
                message=f"De : {name} ({email})\nNuméro : {number}\n\n{message}",
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('home')  # Redirection pour éviter les resoumissions
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})

def success_view(request):
    return HttpResponse("Merci ! Votre message a bien été envoyé.")
