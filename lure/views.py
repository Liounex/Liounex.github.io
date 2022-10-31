from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from lure.forms import ContactForm

# Create your views here.
def Home(request):
    return render(request, 'lure/index.html')

def About(request):
    return render(request, 'lure/nosotros.html')

def Product(request):
    return render(request, 'lure/productos.html')

class Contact(TemplateView):
    template_name = 'lure/contacto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()

        return context

    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            body = render_to_string(
                'lure/email_content.html', {
                    'name': name,
                    'email':email,
                    'message' : message,
                },
                )

            email_message = EmailMessage(
                subject = 'Nuevo Mensaje',
                body = body,
                from_email = email,
                to = ['pbbanger32@gmail.com']
            )

            email_message.content_subtype = 'html'
            email_message.send()
            #print(f"Nombre \n{name}")
            #print("-------------------------")
            #print(f"Correo electronico \n{email}")
            #print("-------------------------")
            #print(f"Mensaje \n{message}")

            return redirect('contacto')
        except:
            return render(request, 'lure/error.html')
        
