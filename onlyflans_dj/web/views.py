from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ContactForm, Flan
from .forms import ContactFormForm


# Create your views here.
def indice(request):
    flanes = Flan.objects.all()
    flanes_pub = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {"flanes_pub": flanes_pub})

def acerca(request):
    return render(request, 'about.html', {})

def bienvenido(request):
    flanes_priv = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {"flanes_pub": flanes_priv})

def contact(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)

            return HttpResponseRedirect("/")
    else:
        form = ContactFormForm
    return render(request, "contact.html",{"form": form})
