from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth import (authenticate, login, logout)
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import SignUpForm , LoginForm
from .models import CreateUser

# Create your views here.

class Register(CreateView):
    template_name = 'sign/index.html'
    success_url   = reverse_lazy('home')
    model = CreateUser
    form_class = SignUpForm
    def form_valid(self, form):
        password = form.cleaned_data['Pass']
        instance = form.instance
        instance.password = make_password(password)
        instance.save()
        login(self.request, instance)
        return super(Register, self).form_valid(form)

def Login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            Email = form.cleaned_data['Email']
            Password = form.cleaned_data['Pass']
            user = authenticate(request=request, Email=Email, Password=Password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('login'))
    else:
        form = LoginForm()
    return render(request, 'sign/login.html', {"form": form})  
 