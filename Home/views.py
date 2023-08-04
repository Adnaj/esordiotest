from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Projectimage
from .forms import ContactMessageForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,"index.html")


def about(request):
    return HttpResponse("about")


def projects(request):
    projet_details={
        'details':Projectimage.objects.all()
    }
    return render(request,"projects.html",projet_details)


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            
            subject = 'New Contact Form Submission'
            message = f'Name: {form.cleaned_data["name"]}\nPhonenumber: {form.cleaned_data["phonenumber"]}\nEmail: {form.cleaned_data["email"]}\nMessage: {form.cleaned_data["message"]}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['adnajnaju01@gmail.com']  # Replace with the recipient's email address

            send_mail(subject, message, from_email, recipient_list)
            
            return render(request, 'contact.html', {'form': ContactMessageForm(), 'success_message': True})
        else:
            return render(request, 'contact.html', {'form': form, 'fail_message': True})
    else:
        form = ContactMessageForm()
    return render(request,"contact.html")
