from django.shortcuts import render
from .forms import BecomeForm
from django.core.mail import send_mail
from pract_2.settings import EMAIL_HOST_USER

def become(request):
    if request.method=="POST":
        form = BecomeForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            name = form['name']
            school = form['school']
            city = form['city']
            email = form['email']
            phone = form['phone']
            #transcript = form['transcript']
            #print(transcript)
            anything_else = form['anything_else']

            send_mail(
                'NEW TUTOR',
                'Name: %s. School: %s. City: %s. Email: %s. Phone: %s. Other: %s.' % (name, school, city, email, phone, anything_else),
                email,
                [EMAIL_HOST_USER],
                fail_silently=True
            )
            context = {'name': name, 'email': email}
            template = 'become/applied.html'

    else: 
        template = 'become/become.html'
        context = {'form': BecomeForm}
    return render(request, template, context)
