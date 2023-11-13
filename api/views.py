from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'api/login.html', {})
    
    def post(self, request):
        data = dict()
        data['username'] = request.POST.get('username')
        data['password'] = request.POST.get('password')

        user = authenticate(**data)
        if user is not None:
            login(request, user)

class RegistrationView(View):
    def get(self, request):
        return render(request, 'api/Registration.html', {})
    
    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user, status = User.objects.get_or_create(username=username)
        if status:
            # new user
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.set_password(password)
            user.save()
            messages.success(request, 'Profile created!')
        else:
            messages.error(request, 'Username already taken!')
        return redirect('register')
    

class AppView(TemplateView):
    template_name = 'index.html'    # react app.