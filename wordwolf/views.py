from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# Create your views here.
def home(request):
    return render(request, 'wordwolf/home.html', {})

@login_required
def private_page(request):
    return render(request, 'wordwolf/private.html', {})

def public_page(request):
    return render(request, 'wordwolf/public.html', {})