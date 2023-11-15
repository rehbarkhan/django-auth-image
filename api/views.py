from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


"""
    Django View Logic
"""
class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('app')
        return render(request, 'api/login.html', {})
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('app')
        data = dict()
        data['username'] = request.POST.get('username')
        data['password'] = request.POST.get('password')

        user = authenticate(**data)
        if user is not None:
            login(request, user)
            return redirect('app')
        else:
            messages.error(request,'Login failed, try again.')
            return redirect('index')

class RegistrationView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('app')
        return render(request, 'api/Registration.html', {})
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('app')
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
    

class AppView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'    # react app.

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('index')

    def post(self, request):
        return self.get(request)
    

# Downlaod Protected File
from django.conf import settings
from django.http import HttpResponse, Http404, FileResponse
from wsgiref.util import FileWrapper
import os
from pathlib import Path    
class DownloadView(LoginRequiredMixin, View):
    def get(self, request, pk):
        base_dir = settings.BASE_DIR
        file_to_dowbload = VideoFile.objects.get(uploaded_by = request.user, id=pk)
        file_path = os.path.join(base_dir,"storage" , str(file_to_dowbload.video_file))
        
        path = Path(file_path)
        with path.open(mode='rb') as fh:
           response = HttpResponse(fh.read(), content_type="image/jpeg")
           response['Content-Disposition'] = 'attachment; filename=MyImage.jpg'
           return response 
        raise Http404
        
    

"""

 DRF View

"""

from rest_framework.viewsets import ModelViewSet
from .models import VideoFile, VideoDescription
from .serializers import VideoFileSer, VideoDescriptionSer

class VideoAPIView(ModelViewSet):
    serializer_class = VideoFileSer
    def get_queryset(self):
        query = VideoFile.objects.filter(uploaded_by = self.request.user)
        return query
    
    def perform_create(self, serializer):
        serializer.save(uploaded_by = self.request.user)



class VideoDescriptionAPIView(ModelViewSet):
    serializer_class = VideoDescriptionSer
    def get_queryset(self):
        query = VideoDescription.objects.filter(created_by = self.request.user)
        return query
    
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)