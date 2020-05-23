from django.shortcuts import render, redirect
from django.urls import reverse
from contact.forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.


def contact(request):
    print('Tipo de peticion {}'.format(request.method))
    contactForm =   ContactForm()
    if request.method == 'POST':
        contactForm        =   ContactForm(request.POST)
        if contactForm.is_valid():
            name        =   request.POST.get('name')
            email       =   request.POST.get('email')
            content     =   request.POST.get('content')
            email       =   EmailMessage(
                subject='Messaje from contact form django',
                body='De {} <{}>\n\nEscribio:\n\n{}'.format(name, email, content),
                from_email='no-contestar@inbox.mailtrap.io',
                to=['16a47ee198-dc7739@inbox.mailtrap.io', ],
                reply_to=[email,]
            )
            try:
                email.send()
                # if all is OK
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?fail')
                
    return render(request, 'contact/contact.html', {'form':contactForm})
